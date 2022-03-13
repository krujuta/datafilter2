# “Filter Section” of an e-commerce app. 

The project that we like you to develop needs to meet the following requirements.

Please check each box as you implement them:  
 Create a back-end structure for a product marketplace. This structure must contain
at least the price, the vendor, the category, a product description, an image, and the admissible region (EU, US, China, ROW) for a given product.  
 The product category should allow at least for sub-categories (two-level taxonomy).  
 Write an API that allows the marketplace front-end to list the products sorted by price,
by vendors, and categories. (Sorting = show all products in the given order)  
 Extend the API by filters for a given category & sub-category, by vendors, and by price. (Filtering = filter products according to given criteria. I.e., show only the matches)


# App specifications
The app is based on Django-Python.\
Database used : Postgresql - hosted on Heroku\
Dockerfile to containerize the application

# How to Run the App :

- Run app locally 

python3 manage.py makemigrations datafilter2  
python3 manage.py migrate datafilter2 - to create schemas

python3 manage.py runserver 8080 - to run app locally 

- To run the app using docker  : 

docker run -d --name datafilter2 -e "PORT=8765" -e "DEBUG=1" --env-file ./env -p 8007:8765 web:latest  
- env file is shared via email.

# API reference :

1. Get products :  

    https://localhost:8007/datafilter2/products :
    - Serves as function view
    - To display products data
    - To add new product  

2. Get product by id : [GET]  

    https://localhost:8007/datafilter2/get_product_by_id/<name>
    
    Get product details by id using name as a parameter
3. Get products with params : [GET]\
    https://localhost:8007/datafilter2/datafilter2/get_products 

    - Query Parameters :  
        a. sort_by = attribute name e.g. price, vendor\
        b. order_by = DESC - to sort values in descending order, if order_by value is not passed, it is ASC order by default.
        c. filter_by = <category=name> or <sub_category=name>

        example :  
        1. Sort products by price ASC
        https://localhost:8007/datafilter2/datafilter2/get_products?sort_by=price  
        2. Sort products by price DESC
         https://localhost:8007/datafilter2/datafilter2/get_products?sort_by=price&order_by=DESC 
        3. Filter products by category
        https://localhost:8007/datafilter2/datafilter2/get_products?filter_by='category=lifestyle'
        3. Filter products by sub_category
        https://localhost:8007/datafilter2/datafilter2/get_products?filter_by='sub_category=accessories'
         



