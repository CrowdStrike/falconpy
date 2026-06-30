"""Type stubs for intelligence_feeds."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class IntelligenceFeeds(ServiceClass):

    def download_feed(
        self,
        *,
        feed_item_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_feeds(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_feeds(
        self,
        *,
        feed_name: Optional[str] = None,
        feed_interval: Optional[str] = None,
        since: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    DownloadFeedArchive = download_feed
    ListFeedTypes = list_feeds
    QueryFeedArchives = query_feeds
