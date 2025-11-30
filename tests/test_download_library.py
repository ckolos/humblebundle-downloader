from humblebundle_downloader.download_library import DownloadLibrary


###
# _should_download_file_by_ext
###
def test_include_logic_has_values():
    dl = DownloadLibrary(
        "fake_library_path",
        ext_include=["pdf", "EPub"],
    )
    assert dl._should_download_file_by_ext("pdf") is True
    assert dl._should_download_file_by_ext("df") is False
    assert dl._should_download_file_by_ext("ePub") is True
    assert dl._should_download_file_by_ext("mobi") is False


def test_include_logic_empty():
    dl = DownloadLibrary(
        "fake_library_path",
        ext_include=[],
    )
    assert dl._should_download_file_by_ext("pdf") is True
    assert dl._should_download_file_by_ext("df") is True
    assert dl._should_download_file_by_ext("EPub") is True
    assert dl._should_download_file_by_ext("mobi") is True


def test_exclude_logic_has_values():
    dl = DownloadLibrary(
        "fake_library_path",
        ext_exclude=["pdf", "EPub"],
    )
    assert dl._should_download_file_by_ext("pdf") is False
    assert dl._should_download_file_by_ext("df") is True
    assert dl._should_download_file_by_ext("ePub") is False
    assert dl._should_download_file_by_ext("mobi") is True


def test_exclude_logic_empty():
    dl = DownloadLibrary(
        "fake_library_path",
        ext_exclude=[],
    )
    assert dl._should_download_file_by_ext("pdf") is True
    assert dl._should_download_file_by_ext("df") is True
    assert dl._should_download_file_by_ext("EPub") is True
    assert dl._should_download_file_by_ext("mobi") is True


###
# _should_download_platform
###
def test_download_platform_filter_none():
    dl = DownloadLibrary(
        "fake_library_path",
        platform_include=None,
    )
    assert dl._should_download_platform("ebook") is True
    assert dl._should_download_platform("audio") is True


def test_download_platform_filter_blank():
    dl = DownloadLibrary(
        "fake_library_path",
        platform_include=[],
    )
    assert dl._should_download_platform("ebook") is True
    assert dl._should_download_platform("audio") is True


def test_download_platform_filter_audio():
    dl = DownloadLibrary(
        "fake_library_path",
        platform_include=["audio"],
    )
    assert dl._should_download_platform("ebook") is False
    assert dl._should_download_platform("audio") is True
