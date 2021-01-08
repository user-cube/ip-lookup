import argparse
import os
from tabulate import tabulate
import geoip2.database


class IPLookup:
    def __init__(self):
        self.database = os.getenv("DATABASE_PATH")

    def _find_ip_info(self, ip_address: str) -> list:
        try:
            with geoip2.database.Reader(self.database + 'GeoLite2-City.mmdb') as reader:
                response = reader.city(ip_address=ip_address)
                code = response.country.iso_code
                country_name = response.country.name
                subdivision = response.subdivisions.most_specific.name
                subdivision_code = response.subdivisions.most_specific.iso_code
                city = response.city.name
                postal = response.postal.code
                latitude = str(response.location.latitude)
                longitude = str(response.location.longitude)
            with geoip2.database.Reader(self.database + 'GeoLite2-ASN.mmdb') as reader:
                response = reader.asn(ip_address=ip_address)
                autonomous_number = response.autonomous_system_number
                organization = response.autonomous_system_organization
            content = [code, country_name, subdivision, subdivision_code, city, postal, latitude, longitude,
                       autonomous_number, organization]
            return content
        except Exception as e:
            print(e)
            return []

    def main(self) -> None:
        headers = ["Code", "Country", "SS", "SC", "City", "Postal Code", "Latitude", "Longitude", "AN", "ASN"]
        if LIST_OF_IPS != "":
            ips = LIST_OF_IPS.split(" ")
            if len(ips) > 0:
                table = []
                for ip in ips:
                    info = self._find_ip_info(ip)
                    if info:
                        table.append(info)
                if table:
                    print(tabulate(table, headers, tablefmt="grid"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ips", help="Search information about a list of IP Addresses", default="")
    args = parser.parse_args()
    LIST_OF_IPS = args.ips
    IPLookup().main()
