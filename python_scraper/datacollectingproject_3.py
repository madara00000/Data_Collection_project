from bs4 import BeautifulSoup
import requests
import mysql.connector

#connecting to the database
def connect_to_database():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "rootroot",
       #change this part ^ so it suits ur infos 

       #"database": "datacollectingproject_database"   
       # we won't need it cuz there is a function to create the DB
    }
    connection = mysql.connector.connect(**db_config)
    if connection:
        print("Database Connected")
        return connection  

#creating the table in mysql
def create_database_and_table(connection):
     # i used this way  to give the sql commands cuz python confuses multi line comments with multi line strings
    create_table_query = "CREATE DATABASE IF NOT EXISTS companies;"
    create_table_query += "USE companies; DROP TABLE IF EXISTS offices;"
    create_table_query += "CREATE TABLE  IF NOT EXISTS offices ("
    create_table_query += "    id INT AUTO_INCREMENT PRIMARY KEY,"
    create_table_query += "    name VARCHAR(255),"
    create_table_query += "    industry VARCHAR(255),"
    create_table_query += "    mobile VARCHAR(255),"
    create_table_query += "    landlinemobile VARCHAR(255),"
    create_table_query += "    email VARCHAR(255),"
    create_table_query += "    address VARCHAR(255),"
    create_table_query += "    link VARCHAR(255)"   
    create_table_query += ");"

    cursor = connection.cursor()

    #in this part i split the commands (/string) so i can execute them one by one
    queries = create_table_query.split(';')
    for query in queries :
        cursor.execute(query)
        cursor.fetchall()
    connection.commit()
    cursor.close()
    print("Table and DB created successfully")


    
# data scraping
def scrap_data(base_url, companies_urls, db_connection):
    company_data = []

    for companyurl in companies_urls:
        url = base_url + companyurl
        response = requests.get(url)
        print(response)

        htmlcontent = BeautifulSoup(response.text, "html.parser")
        caption_div = htmlcontent.find("div", class_="_jb_summary")

        # to find the name of the company
        title_div = caption_div.find("div", class_="_jb_summary_caption")
        title = title_div.find("h1").text


        # to find the  industry, mobile,,landlinemobile, email, address:
        body_div = htmlcontent.find("div", class_="_jb_summary_body")
        target_list = body_div.find("ul")
        
        websiteelement_div = body_div.find("div",class_="mt-3 text-center")
        websiteelement = websiteelement_div.find("a")
        link = websiteelement['href']

        li_elements = target_list.find_all("li")
        if li_elements:
            industry = li_elements[0].find("span").get_text(strip=True)
            email = li_elements[1].find("span").get_text(strip=True)
            mobile = li_elements[2].find("span").get_text(strip=True)
            landlinemobile = li_elements[3].find("span").get_text(strip=True)
            address = li_elements[4].find("span").get_text(strip=True)

            company_data.append((title, industry, mobile,landlinemobile, email, address,link))
        




      #testing the data existance
        #print(f"names : {title}")
       # print(f"emails : {email}")
       # print(f"mobile numbrs : {mobile}")
       # print(f"lanline mobile number :{landlinemobile}")
       # print(f"addressess : {address}")
       # print(f"ind : {industry}")
       # print(f"link = {link}")

    #inserting to the db
    insert_query = "INSERT INTO offices (name, industry, mobile , landlinemobile , email, address , link) VALUES (%s,%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.executemany(insert_query, company_data)
    db_connection.commit()
 
    cursor.close()
    print("Data insertion complete!")

#  usage
if __name__ == "__main__":
    try : 
        db_connection = connect_to_database()
        if db_connection:
        

            create_database_and_table(db_connection)

            # since every company has its own URL 
            # i chose to enter the page of each company and scrap its data 
            # i'm using this method so i can avoid protected data in the main link that includes all the companies:

            base_url = "https://www.yenino.com/ma-en/company/"
            companies_urls = ["webkech-agence-de-communication-1411",
                               "inmorocco-solutions-sarl-1412", 
                               "seo-com-1413",
                                "agence-de-communication-web-marrakech-1414",
                                "gudiz-1462",
                                "sasai-global-2239", 
                                "tasyiercom-full-service-digital-marketing-agency-2726"
                                ,"agence-web-marrakech-2867",
                                "buystealthaccounts-5981",
                                "devxco-6155",
                                "inco-media-digital-marketing-agency-in-casablanca-6308",
                                "elvisuel-6350",
                                "bionic-intel-7056",
                                "buystealthaccounts-7718",
                                "aev-tech",
                                "digital-spread",
                                "fusion-bpo-services",
                                "ma-lex-centre-daffaires-creation-entreprise-a-tanger-domiciliation-tanger-fiduciaire-a-tanger-creation-societe-tanger-maroc-depot-de-marque",
                                
                                ]

            scrap_data(base_url, companies_urls, db_connection)
        
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error at creating the db and table: {err} ")
    except Exception as e:
        print("Error at scraping the data:", str(e))

