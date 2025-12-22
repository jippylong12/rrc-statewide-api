from typing import Iterator, Dict, Any, Optional
from dbfread import DBF
from .utils import construct_api_number, format_lease_id, format_district

class RRCStatewideParser:
    """
    Parser for Texas RRC Statewide API Data in DBF format.
    """

    def __init__(self, dbf_path: str, encoding: str = "iso-8859-1"):
        """
        Initialize the parser.
        
        Args:
            dbf_path: Path to the .dbf file.
            encoding: Character encoding of the DBF file (default: iso-8859-1).
        """
        self.dbf_path = dbf_path
        self.encoding = encoding

    def parse(self) -> Iterator[Dict[str, Any]]:
        """
        Yields normalized records from the DBF file.
        
        Returns:
            Iterator of dictionaries containing record data.
        """
        table = DBF(self.dbf_path, encoding=self.encoding, char_decode_errors='replace')
        
        for record in table:
            yield self._normalize_record(record)

    def _normalize_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize raw DBF record fields.
        
        Args:
            record: Raw record dictionary.
            
        Returns:
            Normalized record dictionary.
        """
        # Create a clean copy to avoid mutating the original dbfread object immediately if referenced elsewhere
        data = dict(record)
        
        # Normalize keys to uppercase (standard practice for RRC DBF, but ensuring consistency)
        data = {k.upper(): v for k, v in data.items()}
        
        # Construct full API Number if component parts exist
        if 'API' in data:
            # Some files might just have 'API', others might need construction. 
            # Assuming 'API' is the unique identifier or component. 
            # If standard 8-digit or 12-digit parts are split, we handle them here.
            # For now, we assume the API field exists or is constructed from COUNTY + UNIQUE ID
            # Adjust based on specific RRC file layout documentation if needed.
            pass

        # Apply specific formatting helpers if fields exist
        if 'DISTRICT' in data:
            data['DISTRICT'] = format_district(data['DISTRICT'])
            
        return data
