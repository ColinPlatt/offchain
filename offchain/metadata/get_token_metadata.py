from typing import Optional, Union

from offchain.metadata.models import (
    Metadata,
    MetadataProcessingError,
    Token,
)

from offchain.metadata.pipelines.metadata_pipeline import MetadataPipeline


def get_token_metadata(
    collection_address: str,
    token_id: int,
    chain_identifier: str = "CANTO-MAINNET",
    uri: Optional[str] = None,
) -> Union[Metadata, MetadataProcessingError]:
    token = Token(
        collection_address=collection_address,
        token_id=token_id,
        chain_identifier=chain_identifier,
        uri=uri,
    )
    return MetadataPipeline().run([token])[0]
