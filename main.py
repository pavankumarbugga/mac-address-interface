import requests
import sys
import creds


def main():
    # Check if mac-address argument is provided
    if (len(sys.argv) != 2):
        sys.exit('Invalid number of arguments')
    
    macadd = sys.argv[1]
    URL = f'https://api.macaddress.io/v1?apiKey={creds.api_key}&output=json&search={macadd}'
    res = requests.get(URL)
    if (res.status_code == 200):
        jsondata = res.json()
        print(jsondata['vendorDetails']['companyName'])
    elif (res.status_code == 401):
        print("Access restricted. Enter the correct API key.")
    elif (res.status_code == 402):
        print("Access restricted. Check the credits balance.")
    elif (res.status_code == 422):
        print("Invalid MAC or OUI address was received.")
    elif (res.status_code == 429):
        print("Too many requests. Try your call again later.")
    elif (res.status_code == 500):
        print("Internal server error. Try your call again or contact us.")
    else:
        print("Failure")


if __name__ == '__main__':
    main()