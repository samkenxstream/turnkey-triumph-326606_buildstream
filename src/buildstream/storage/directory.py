#!/usr/bin/env python3
#
#  Copyright (C) 2018 Bloomberg Finance LP
#  Copyright (C) 2022 Codethink Ltd
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Authors:
#        Jim MacArthur <jim.macarthur@codethink.co.uk>
#        Tristan van Berkom <tristan.vanberkom@codethink.co.uk>

"""
Directory
=========

This is a virtual Directory class to isolate the rest of BuildStream
from the backing store implementation.  Sandboxes are allowed to read
from and write to the underlying storage, but all others must use this
Directory class to access files and directories in the sandbox.

See also: :ref:`sandboxing`.

"""


from contextlib import contextmanager
from tarfile import TarFile
from typing import Callable, Optional, Union, List, IO, Iterator

from .._exceptions import BstError
from ..exceptions import ErrorDomain
from ..utils import BST_ARBITRARY_TIMESTAMP, FileListResult


class DirectoryError(BstError):
    """Raised by Directory functions.

    It is recommended to handle this error and raise a more descriptive
    user facing :class:`.ElementError` or :class:`.SourceError` from this error.

    If this is not handled, the BuildStream core will fail the current
    task where the error occurs and present the user with the error.
    """

    def __init__(self, message: str, reason: str = None):
        super().__init__(message, domain=ErrorDomain.VIRTUAL_FS, reason=reason)


class FileMode:
    """Depicts the type of a file"""

    def __init__(
        self, *, regular: bool = False, directory: bool = False, symlink: bool = False, executable: bool = False
    ) -> None:
        self.regular: bool = regular
        """Whether this is a regular file"""

        self.directory: bool = directory
        """Whether this is a directory"""

        self.symlink: bool = symlink
        """Whether this is a symbolic link"""

        self.executable: bool = executable
        """Whether this file is executable"""


class FileStat:
    """Depicts stats about a file"""

    def __init__(self, mode: FileMode, *, size: int = 0, mtime: float = BST_ARBITRARY_TIMESTAMP) -> None:

        self.mode: FileMode = mode
        """The file type"""

        self.size: int = size
        """The size of the file in bytes"""

        self.mtime: float = mtime
        """The modification time of the file"""


class Directory:
    def __init__(self, external_directory=None):
        raise NotImplementedError()

    def __iter__(self) -> Iterator[str]:
        raise NotImplementedError()

    ###################################################################
    #                           Public API                            #
    ###################################################################

    def descend(self, *path: str, create: bool = False, follow_symlinks: bool = False) -> "Directory":
        """Descend one or more levels of directory hierarchy and return a new
        Directory object for that directory.

        Args:
           *path: A list of strings which are all directory names.
           create: If this is true, the directories will be created if
                   they don't already exist.

        Returns:
           A Directory object representing the found directory.

        Raises:
           DirectoryError: if any of the components in subdirectory_spec
                           cannot be found, or are files, or symlinks to files.
        """
        raise NotImplementedError()

    # Import and export of files and links
    def import_files(
        self,
        external_pathspec: Union["Directory", str],
        *,
        filter_callback: Optional[Callable[[str], bool]] = None,
        can_link: bool = False,
    ) -> FileListResult:
        """Imports some or all files from external_path into this directory.

        Args:
           external_pathspec: Either a string containing a pathname, or a
                              Directory object, to use as the source.
           filter_callback: Optional filter callback. Called with the
                            relative path as argument for every file in the source directory.
                            The file is imported only if the callable returns True.
                            If no filter callback is specified, all files will be imported.
           can_link: Whether it's OK to create a hard link to the original content, meaning the stored copy will change
                     when the original files change. Setting this doesn't guarantee hard links will be made.

        Returns:
           A :class:`.FileListResult` report of files imported and overwritten.

        Raises:
           DirectoryError: if any system error occurs.
        """
        return self._import_files_internal(external_pathspec, filter_callback=filter_callback, can_link=can_link,)

    def import_single_file(self, external_pathspec: str) -> FileListResult:
        """Imports a single file from an external path

        Args:
           external_pathspec: A string containing a pathname.
           properties: Optional list of strings representing file properties to capture when importing.

        Returns:
           A :class:`.FileListResult` report of files imported and overwritten.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def export_files(self, to_directory: str, *, can_link: bool = False, can_destroy: bool = False) -> None:
        """Copies everything from this into to_directory.

        Args:
           to_directory: a path outside this directory object where the contents will be copied to.
           can_link: Whether we can create hard links in to_directory instead of copying.
                     Setting this does not guarantee hard links will be used.
           can_destroy: Can we destroy the data already in this directory when exporting? If set,
                        this may allow data to be moved rather than copied which will be quicker.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def export_to_tar(self, tarfile: TarFile, destination_dir: str, mtime: int = BST_ARBITRARY_TIMESTAMP) -> None:
        """ Exports this directory into the given tar file.

        Args:
          tarfile: A Python TarFile object to export into.
          destination_dir: The prefix for all filenames inside the archive.
          mtime: mtimes of all files in the archive are set to this.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    # Convenience functions
    def is_empty(self) -> bool:
        """ Return true if this directory has no files, subdirectories or links in it.
        """
        raise NotImplementedError()

    def list_relative_paths(self) -> Iterator[str]:
        """Provide a list of all relative paths in this directory.

        Includes directories only if they are empty.

        Yields:
           All files in this directory with relative paths.
        """
        raise NotImplementedError()

    def get_size(self) -> int:
        """ Get an approximation of the storage space in bytes used by this directory
        and all files and subdirectories in it. Storage space varies by implementation
        and effective space used may be lower than this number due to deduplication. """
        raise NotImplementedError()

    def exists(self, *path: str, follow_symlinks: bool = False) -> bool:
        """ Check whether the specified path exists.

        Args:
          *path: A list of strings which are all path components.
          follow_symlinks: True to follow symlinks.

        Returns:
           True if the path exists, False otherwise.
        """
        raise NotImplementedError()

    def stat(self, *path: str, follow_symlinks: bool = False) -> FileStat:
        """ Get the status of a file.

        Args:
          *path: A list of strings which are all path components.
           follow_symlinks: True to follow symlinks.

        Returns:
           A :class:`.FileStat` object.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    @contextmanager
    def open_file(self, *path: str, mode: str = "r") -> Iterator[IO]:
        """ Open file and return a corresponding file object. In text mode,
        UTF-8 is used as encoding.

        Args:
           *path: A list of strings which are all path components.
           mode (str): An optional string that specifies the mode in which the file is opened.

        Yields:
           The file object for the open file

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def file_digest(self, *path: str) -> str:
        """ Return a digest of a file. The digest algorithm is implementation-
        defined.

        Args:
           *path: A list of strings which are all path components.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def readlink(self, *path: str) -> str:
        """ Return a string representing the path to which the symbolic link points.

        Args:
           *path: A list of strings which are all path components.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def remove(self, *path: str, recursive: bool = False) -> None:
        """ Remove a file, symlink or directory. Symlinks are not followed.

        Args:
          *path: A list of strings which are all path components.
          recursive: True to delete non-empty directories.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def rename(self, src: List[str], dest: List[str]) -> None:
        """ Rename a file, symlink or directory. If destination path exists
        already and is a file or empty directory, it will be replaced.

        Args:
          *src: Source path components.
          *dest: Destination path components.

        Raises:
           DirectoryError: if any system error occurs.
        """
        raise NotImplementedError()

    def isfile(self, *path: str, follow_symlinks: bool = False) -> bool:
        """ Check whether the specified path is an existing regular file.

        Args:
           *path: A list of strings which are all path components.
           follow_symlinks: True to follow symlinks.

        Returns:
           True if the path is an existing regular file, False otherwise.
        """
        try:
            st = self.stat(*path, follow_symlinks=follow_symlinks)
            return st.mode.regular
        except DirectoryError:
            return False

    def isdir(self, *path: str, follow_symlinks: bool = False) -> bool:
        """ Check whether the specified path is an existing directory.

        Args:
          *path: A list of strings which are all path components.
           follow_symlinks: True to follow symlinks.

        Returns:
           True if the path is an existing directory, False otherwise.
        """
        try:
            st = self.stat(*path, follow_symlinks=follow_symlinks)
            return st.mode.directory
        except DirectoryError:
            return False

    def islink(self, *path: str, follow_symlinks: bool = False) -> bool:
        """ Check whether the specified path is an existing symlink.

        Args:
           *path: A list of strings which are all path components.
           follow_symlinks: True to follow symlinks.

        Returns:
           True if the path is an existing symlink, False otherwise.
        """
        try:
            st = self.stat(*path, follow_symlinks=follow_symlinks)
            return st.mode.symlink
        except DirectoryError:
            return False

    ###################################################################
    #                         Internal API                            #
    ###################################################################

    # _import_files_internal()
    #
    # Internal API for importing files, which exposes a few more parameters than
    # the public API exposes.
    #
    # Args:
    #   external_pathspec: Either a string containing a pathname, or a
    #                      Directory object, to use as the source.
    #   filter_callback: Optional filter callback. Called with the
    #                    relative path as argument for every file in the source directory.
    #                    The file is imported only if the callable returns True.
    #                    If no filter callback is specified, all files will be imported.
    #                    update_mtime: Update the access and modification time of each file copied to the time specified in seconds.
    #   can_link: Whether it's OK to create a hard link to the original content, meaning the stored copy will change
    #                     when the original files change. Setting this doesn't guarantee hard links will be made.
    #   properties: Optional list of strings representing file properties to capture when importing.
    #
    # Returns:
    #    A :class:`.FileListResult` report of files imported and overwritten.
    #
    # Raises:
    #    DirectoryError: if any system error occurs.
    #
    def _import_files_internal(
        self,
        external_pathspec: Union["Directory", str],
        *,
        filter_callback: Optional[Callable[[str], bool]] = None,
        update_mtime: Optional[float] = None,
        can_link: bool = False,
        properties: Optional[List[str]] = None,
    ) -> FileListResult:
        return self._import_files(
            external_pathspec,
            filter_callback=filter_callback,
            update_mtime=update_mtime,
            can_link=can_link,
            properties=properties,
        )

    # _import_files()
    #
    # Abstract method for backends to import files from an external directory
    #
    # Args:
    #   external_pathspec: Either a string containing a pathname, or a
    #                      Directory object, to use as the source.
    #   filter_callback: Optional filter callback. Called with the
    #                    relative path as argument for every file in the source directory.
    #                    The file is imported only if the callable returns True.
    #                    If no filter callback is specified, all files will be imported.
    #                    update_mtime: Update the access and modification time of each file copied to the time specified in seconds.
    #   can_link: Whether it's OK to create a hard link to the original content, meaning the stored copy will change
    #                     when the original files change. Setting this doesn't guarantee hard links will be made.
    #   properties: Optional list of strings representing file properties to capture when importing.
    #
    # Returns:
    #    A :class:`.FileListResult` report of files imported and overwritten.
    #
    # Raises:
    #    DirectoryError: if any system error occurs.
    #
    def _import_files(
        self,
        external_pathspec: Union["Directory", str],
        *,
        filter_callback: Optional[Callable[[str], bool]] = None,
        update_mtime: Optional[float] = None,
        can_link: bool = False,
        properties: Optional[List[str]] = None,
    ) -> FileListResult:
        raise NotImplementedError()

    # _get_underlying_path()
    #
    # Args:
    #    filename: The name of the file in this directory
    #
    # Returns the underlying (real) file system path for the file in this
    # directory
    #
    # Raises:
    #    DirectoryError: if the backend doesn't use local files, or if
    #                    there is no such file in this directory
    #
    def _get_underlying_path(self, filename) -> str:
        raise NotImplementedError()

    # _get_underlying_directory()
    #
    # Returns the underlying (real) file system directory this
    # object refers to.
    #
    # Raises:
    #    DirectoryError: if the backend doesn't have an underlying directory
    #
    def _get_underlying_directory(self) -> str:
        raise NotImplementedError()

    # _set_deterministic_user():
    #
    # Abstract method to set all files in this directory to the current user's euid/egid.
    #
    def _set_deterministic_user(self):
        raise NotImplementedError()

    # _create_empty_file()
    #
    # Utility function to create an empty file
    #
    def _create_empty_file(self, *path):
        with self.open_file(*path, mode="w"):
            pass
