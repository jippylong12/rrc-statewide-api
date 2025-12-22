from typing import Optional, Union

def construct_api_number(county_code: Union[str, int], unique_id: Union[str, int]) -> str:
    """
    Construct a standard API number (CCC-UUUUU).
    RRC API numbers often usually generally 8 digits: 3 for county, 5 for unique id.
    
    Args:
        county_code: 3-digit county code.
        unique_id: 5-digit unique identifier.
        
    Returns:
        Formatted API string (e.g., '105-12345').
    """
    return f"{int(county_code):03d}-{int(unique_id):05d}"

def format_lease_id(lease_id: Union[str, int], lease_type: str = 'oil') -> str:
    """
    Format lease ID with appropriate padding.
    Oil: 5 digits
    Gas: 6 digits
    
    Args:
        lease_id: Raw lease ID.
        lease_type: 'oil' or 'gas'.
        
    Returns:
        Padded lease ID string.
    """
    id_val = int(lease_id) if str(lease_id).isdigit() else 0
    if lease_type.lower() == 'gas':
        return f"{id_val:06d}"
    return f"{id_val:05d}"
    
def format_district(district_code: Union[str, int]) -> str:
    """
    Format district code (ensure 2 digits).
    
    Args:
        district_code: Raw district code.
        
    Returns:
        Formatted district string.
    """
    # Handle district '8A' or similar alphanumeric cases if they exist, 
    # but standard numeric ones get 0-padded.
    s_code = str(district_code).strip().upper()
    if s_code.isdigit():
        return f"{int(s_code):02d}"
    return s_code
