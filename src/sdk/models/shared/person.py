"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Person:
    r"""returns the person"""
    
    birth_date: str = dataclasses.field()
    r"""The birth date of the person"""  
    birth_year: float = dataclasses.field()
    r"""The birth year of the person"""  
    certifications: list[str] = dataclasses.field()
    r"""The certifications of the person"""  
    education: list[str] = dataclasses.field()
    r"""The educational history of the person"""  
    emails: list[str] = dataclasses.field()
    r"""The personal and work emails of the person"""  
    experience: list[str] = dataclasses.field()
    r"""The works experience of the person"""  
    facebook_id: str = dataclasses.field()
    r"""The Facebook ID of the person"""  
    facebook_url: str = dataclasses.field()
    r"""The Facebook URL of the person"""  
    facebook_username: str = dataclasses.field()
    r"""The Facebook username of the person"""  
    first_name: str = dataclasses.field()
    r"""The first name of the person"""  
    full_name: str = dataclasses.field()
    r"""The full name of the person"""  
    gender: str = dataclasses.field()
    r"""The gender of the person"""  
    github_url: str = dataclasses.field()
    r"""The Github URL of the person"""  
    github_username: str = dataclasses.field()
    r"""The Github username of the person"""  
    id: float = dataclasses.field()
    r"""The key for looking up the company"""  
    industry: str = dataclasses.field()
    r"""The industry of the person"""  
    inferred_salary: str = dataclasses.field()
    r"""The inferred salary band for the person"""  
    inferred_years_experience: float = dataclasses.field()
    r"""The inferred years of experience for the person"""  
    interests: list[str] = dataclasses.field()
    r"""The interests of the person"""  
    job_company_facebook_url: str = dataclasses.field()
    r"""The current job company Facebook URL"""  
    job_company_founded: str = dataclasses.field()
    r"""The current job company founded year"""  
    job_company_id: str = dataclasses.field()
    r"""The current job company ID"""  
    job_company_industry: str = dataclasses.field()
    r"""The current job company industry"""  
    job_company_linkedin_id: str = dataclasses.field()
    r"""The current job company id on LinkedIn"""  
    job_company_linkedin_url: str = dataclasses.field()
    r"""The current job company LinkedIn URL"""  
    job_company_location_address_line_2: str = dataclasses.field()
    r"""The current job company location street adress second line"""  
    job_company_location_continent: str = dataclasses.field()
    r"""The current job company location continent"""  
    job_company_location_country: str = dataclasses.field()
    r"""The current job company location country"""  
    job_company_location_geo: str = dataclasses.field()
    r"""The current job company location geo coordinates"""  
    job_company_location_locality: str = dataclasses.field()
    r"""The current job company location city"""  
    job_company_location_metro: str = dataclasses.field()
    r"""The current job company location metro"""  
    job_company_location_name: str = dataclasses.field()
    r"""The current job company location name"""  
    job_company_location_postal_code: str = dataclasses.field()
    r"""The current job company location postal code"""  
    job_company_location_region: str = dataclasses.field()
    r"""The current job company location region"""  
    job_company_location_street_address: str = dataclasses.field()
    r"""The current job company location street address"""  
    job_company_name: str = dataclasses.field()
    r"""The current job company name"""  
    job_company_size: str = dataclasses.field()
    r"""The current job company size"""  
    job_company_twitter_url: str = dataclasses.field()
    r"""The current job company Twitter URL"""  
    job_company_website: str = dataclasses.field()
    r"""The current job company website"""  
    job_last_updated: str = dataclasses.field()
    r"""The last update date for the job"""  
    job_start_date: str = dataclasses.field()
    r"""The start date for the current job"""  
    job_summary: str = dataclasses.field()
    r"""The summary for the current job"""  
    job_title: str = dataclasses.field()
    r"""The current job title of the person"""  
    job_title_levels: list[str] = dataclasses.field()
    r"""The current job title levels"""  
    job_title_role: str = dataclasses.field()
    r"""The current job title role of the person"""  
    job_title_sub_role: str = dataclasses.field()
    r"""The current job title sub-role of the person"""  
    languages: list[str] = dataclasses.field()
    r"""The languages of the person"""  
    last_name: str = dataclasses.field()
    r"""The last name of the person"""  
    linkedin_connections: float = dataclasses.field()
    r"""The number of LinkedIn connections for the person"""  
    linkedin_id: float = dataclasses.field()
    r"""The linkedIn ID of the person"""  
    linkedin_url: str = dataclasses.field()
    r"""The linkedIn URL of the person"""  
    linkedin_username: str = dataclasses.field()
    r"""The linkedIn user name of the person"""  
    location_address_line_two: str = dataclasses.field()
    r"""The current location street address second line for the person"""  
    location_continent: str = dataclasses.field()
    r"""The current location continent for the person"""  
    location_country: str = dataclasses.field()
    r"""The current location country for the person"""  
    location_geo: list[str] = dataclasses.field()
    r"""The current location geo coordinates for the person"""  
    location_last_updated: str = dataclasses.field()
    r"""The current location last updated date for the person"""  
    location_locality: str = dataclasses.field()
    r"""The current location city for the person"""  
    location_metro: str = dataclasses.field()
    r"""The current location metro for the person"""  
    location_name: str = dataclasses.field()
    r"""The current location name for the person"""  
    location_postal_code: str = dataclasses.field()
    r"""The current location postal code for the person"""  
    location_region: str = dataclasses.field()
    r"""The current location region for the person"""  
    location_street_address: str = dataclasses.field()
    r"""The current location street address for the person"""  
    middle_initial: str = dataclasses.field()
    r"""The middle initial of the person"""  
    middle_name: str = dataclasses.field()
    r"""The middle name of the person"""  
    mobile_phone: str = dataclasses.field()
    r"""The mobile phone of the person"""  
    phone_numbers: list[str] = dataclasses.field()
    r"""The phone numbers of the person"""  
    profiles: list[str] = dataclasses.field()
    r"""The social profiles of the person"""  
    skills: list[str] = dataclasses.field()
    r"""The skills of the person"""  
    street_addresses: list[str] = dataclasses.field()
    r"""The street addresses of the person"""  
    summary: str = dataclasses.field()
    r"""The self-summary of the person's work experience"""  
    twitter_url: str = dataclasses.field()
    r"""The Twitter URL of the person"""  
    twitter_username: str = dataclasses.field()
    r"""The Twitter username of the person"""  
    work_email: str = dataclasses.field()
    r"""The work email of the person"""  
    