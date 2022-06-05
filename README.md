![Responsive Mockup](/design/wireframes/mockup.png)

# THE GRIND HOUSE
THE GRIND HOUSE is a practical Full Stack Frameworks with Django Milestone Project. 

Heroku App: https://kenweechin-the-grind-house.herokuapp.com/

Github: https://github.com/kenweechin/the_grind_house

The main objective of this project is to create an e-commerce platform that allow users to browse the products on the website, and if they are interested on any particular products, they can subsequently purchase them. This e-commerce project platform is no difference as compare to the other e-commerce platform that existed on the market, but some advance functionality is recommended to implement in the future as this project is to showcase the understanding of the Full Stack Framework concept.
In general, THE GRIND HOUSE offers features of different varieties of coffee maker products accessibility to either registered or non-registered user. They can browse all the products freely on the website and read the top rated products review on the blog site. THE GRIND HOUSE is aiming to create a coffee lover and coffee maker community.

The website consists of:
* Home Page: Landing image with coffee makers as the focus objects, an eye-catching banners showing the free delivery threshold positioned at the top page, different varieties of coffee makers navigation links at the top page as well, a "DISCOVER MORE" button in the middle of the page which directs the user to glance through all the available coffee makers on the page. This button navigation feature offers another way for the user to navigate by one click to browse all the coffee makers if they do not prefer to check the different products on the navigation links. The landing page consists of a blog section which located at the bottom page. User can click in the blog link to see the top selling products. 
* Product Page: Display all coffee makers offers by THE GRIND HOUSE. Each coffee makers consists of it's own image, product description, price, and rating. 
* Product Detail Page: Display the product details with the function of quantity increment and decrement button, add to cart button, and explore more navigation button. A toast notification will pop out after the user clicked on "add to cart" button, and there is a "secure checkout" button. It redirects user to the checkout page.
* Cart page: Display all the products the user have chosen. User can get to know what products are in their cart, with the cart total price showing at visible position of the web page. User will get a toast notification either they update the selected product quantity or remove the product. 
* Checkout Page: User can fill up their personal details in the form provided. Order summary is shown at in the page so user can glance through the products they have chosen, adn the cost breakdown. 
* Checkout Success Page: This page shows the purchase completion and the order detail.
* Profile: Display the default delivery information of the user, update information button, and order details. Non-registered would not have profile page. 
* Blog Page: Display the top products review.
* Blog Detail Page: Display the comments added by the any user. Registered and non registered user can input their comment and subsequently it will show up in the comment section. 
* Log In Page: User can log in to their account.
* Register Page: Non registered user can create an account.

Shopper (non-registered account) page accessibility:
* Home Page
* Product Page
* Product Detail Page
* Cart page
* Checkout Page
* Checkout Success Page
* Blog Page
* Blog Detail Page

Site User (registered account) page accessibility:
* Home Page
* Product Page
* Product Detail Page
* Cart page
* Checkout Page
* Checkout Success Page
* Blog Page
* Blog Detail Page
* Profile Page

Admin page accessibility:
* Home Page
* Product Page
* Product Detail Page
* Cart page
* Checkout Page
* Checkout Success Page
* Blog Page
* Blog Detail Page
* Profile Page
* Product Management Page

## **USER EXPERIENCE (UX)**

### **User Stories**

#### **User Classes:**
* Shopper
* Site User
* Admin - Super User


| STORY ID     | AS A             | I WANT TO BE ABLE TO     | SO THAT I CAN    |   
| -------------| -------------    | --------                 | --------         |
| Viewing and Navigation |
| ID 101  | Shopper  | View a list of products  | Select those I am interested in| 
| ID 102  | Shopper  | View individual product details  | Determine the price, rating, image and volumes availability|
| ID 103  | Shopper  | View my purchases | Ensure I have purchased the products that I want|
| ID 104  | Shopper  | View my cart price total easily | Ensure I keep tracking on my spending |
| Registration and User Accounts|
| ID 201  | Site User| Register for an account | Have a personalised account and be able to access my own profile | 
| ID 202  | Site User| Login or Logout | Access my personal account and view my own profile |
| ID 203  | Site User| Reset my password| Reset password if I forget my password and to improve my account security|
| ID 204  | Site User| Receive registration email confirmation | Verify account registration is successful|
| ID 205  | Site User| Own a personalised user profie | View my purchase history and save my delivery and payment information|
| Sorting and Searching|
| ID 301  | Shopper| Search by name or description|Find a product by searching keyword either matching to the title/descrtiption|
| ID 302  | Shopper| Sort a specific product category | Easily find the products that fall under a specific category.
| ID 303  | Shopper| Sort product pricing | View the pricing from the lowest to the highest in an ascending order. 
| ID 304  | Shopper| Sort product rating | View the rating from the highest to the lowest in a descending order.
| Purchasing and Checkout|
| ID 401  | Shopper| Easily select the volume and quantity of a product| Ensure I don't select the wrong products, volume and quantity |
| ID 402  | Shopper| View my selected products in my cart | Confirm the products selected with selected attributes and total price
| ID 403  | Shopper| Adjust the quantity of an individual product in the cart | Easily make changes before checkout / payment
| ID 404  | Shopper| Easily enter my payment information | Check out quickly with no hassles
| ID 405  | Shopper| Feel my personal and payment information is safe and secure | Confidently provide the essential payment info
| ID 406  | Shopper| View my order confirmation after checkout | Identify if there is any mistake
| ID 407  | Shopper| Receive an email confirmation after checking out | Keep the confirmation of what I've pruchased for my record
| Blog Review|
| ID 501  | Shopper| View the top rated product in one page | Purchase the product on the site more confidently and feeling secure|
| ID 502  | Shopper| Review and write comments on the top rated products | Provide valuable feedback to the other buyers|
| ID 503  | Shopper| View the date of the posted comments | Verify the updated /recent review|
| Admin and Product Management|
| ID 601  | Admin| Add a product | Add new product to the store|
| ID 602  | Admin| Edit or delete a product | Edit the product's image, description, volume and others criteria| 
| ID 603  | Admin| Delete product | Remove products that are sold out or no longer for sale|

# Design
## **DATABASE**
![Database Scheme](/design/database/database.png)
#### **Diagram of website database scheme**

## **STYLING CHOICES**
* Framework
    *[Boostrap](https://getbootstrap.com/), a front-end framework was utilized for this project.
* Imagery
    * The background image of the landing page is using the image with 2 different coffee makers as the main characters with a blur background. This image style can showcase the purpose of the website is trying to show or sell to the shopper. This can attract the shoppers' attention and yield a trust emotion toward the website.
    * The blog image below the landing page in the home page is using a simple combination between coffee, 4 characters and leaf branches. The idea behind this image is to demonstrate the finish product producded by using the coffee maker that the store is selling which tends to create an attract emotion between the shopper and the store.  
* Fonts
    * Playfair Display font was chosen as the main font throughout the website. Playfair Display font looks elegant either as a title or the content on a website.
* Color Scheme
    * Chathams Blue and Internation Orange are the theme colors either for the navigation links, top banners and buttons. The background color is mostly white as it can demonstrate different products that have different colors. 
    * Red color is used for alert notification and alert message.
* Icons
    * [FontAwesome](https://fontawesome.com/) is used for showing the purpose of the navigation links. Icons are great in grabbing users' attention. It is user-friendly and absolutely useful for non-native English speakers and the icons stand out their purpose.  
* Pulse animation effect
    * Show on *Secure Checkout button* and *Complete Order button*. The pulse effect can guide the user to the next stage immediately without taking time to find it. The effect is visually appealing as well.

# Features
## **PAGE LAYOUT**
Balsamiq software was used to generate the following wireframes while doing the project planning and scope plan section. Each wireframes link consists of laptop, tablet and mobile resolution. 

### **NAVIGATION LINKS AND SEARCH BAR**
The navigation links and search bar are span across different pages so the shopper can always direct to any product they wish to view. This creates an easy navigation for the shopper even though if they are in different web page. Shopper can key in any keyword in the search bar and the result will be shown after they clicked on the search button. The search function will search through product title and description, subsequently return found result. They are two possible wrong searching method. The first one will be the empty input. This will return a toast message error displaying *Error! There is no input in the query.* and redirect the shopper back to All Product page. See the image below:
![Empty Input Search Bar](/design/screenshot/empty_input.png)
The second wrong input will be either a gibberish or input that doesn't match to the product title or description in the database. This will return a paragraph displaying *No products found with that search query!.* in red. See the image below:
![Wrong Query](/design/screenshot/wrong_query.png)

#### *Wireframes* 
![Navigation Link](/design/screenshot/navigation_links.png)

### **LANDING PAGE**
The landing page is used to showcase the overall idea of the website/store is trying to cover in their business. The landing image are contained as the first half section of the whole landing page to grab shopper attention, while the bottom part of the page consists of the blog section. There are only a few vital buttons which can direct the shopper to browse the products and the blog page.
#### *Wireframes*  
* [Landing Page](/design/wireframes/landing_page.png)

### **ALL PRODUCTS PAGE**
The all products page displays all the available store products. Each products are aligned visually appealing and all of the images are displaying in a consistent size. The product's price, rating, and description are set in a consistent manner so the shopper can view the details easily when glancing through the page. In the laptop resolution, the products are aligned as 4 in a row, whereas 2 in a row in tablet resolution, and one each in mobile resolution. This layout design is aim to fit the products properly to different devices resolution to avoid any uneccessary blank spaces. 
#### *Wireframes*  
* [All Product](/design/wireframes/products.png)

Furthermore, for the admin user, the *edit and delete* button is shown under each product so that the admin can perform edit on the product's description, price, sku, category, image, whether the product has volume attribute, and rating. This is shown as the image below:
![Product_Edit_Delete](/design/screenshot/admin_product_edit.png)

### **PRODUCT DETAIL PAGE**
Shopper can click on each product from All Product Page and will be directed to the Product Detail Page. This page is showing the product image, description, price, rating, quantity adjustment, volume selection, add to cart button, and explore more button.
#### *Wireframes* 
* [Product Detail](/design/wireframes/product_detail.png)  

Admin user has the accessibility to *edit and delete* in this product detail page. Shown as image below:
![ProductDetail_Edit_Delete](/design/screenshot/product_detail_edit_delete.png)

### **CART PAGE**
The cart page consists of the product image, description, volume if available, corresponding sku, price, quantity adjustment button, cart total, delivery cost, grand total, checkout button and keep shopping button. The cart total is shown at the top page as the title so the shopper can view their total amount to pay easily without scrolling down the page. Shopper and admin can either update the quantity of the specific product or remove the product by clicking on the button right below the quantity adjustment button. Since the free delivery threshold is over €150, hence any amount less than €150, there will be a text at the right bottom corner showing to the buyer the amount needed to get free delivery. It is colored in red so it is easily seen. Shown in the image below: 
![Cart](/design/screenshot/cart.png)
#### *Wireframes* 
* [Cart](/design/wireframes/cart.png)

### **CHECKOUT PAGE**
The checkout page consists of the form where the buyer would have to fill in their required details, option of whether to save their details by clicking on the tick box, and apparently not including the payment details for security reason. There is an order summary on the right side of the page showing the items the buyer is going to purchase. The adjust cart button at the bottom page provide the link for the buyer to make adjustment easily after viewing the summary. This layout ensure the buyer would not make mistake before they make the payment. 
#### *Wireframes* 
* [Checkout](/design/wireframes/checkout.png)

### **CHECKOUT SUCCESS PAGE**
The checkout success page shows the order detail (the forms that buyer has filled in the checkout page) and toast notification at the top right corner of the page displaying the buyer had succeeded to place the order. 
#### *Wireframes* 
* [Checkout Success](/design/wireframes/checkout_success.png)

This is the toast notification wireframes shown as below:
* [Toast](/design/wireframes/toast.png)

### **PROFILE**
The profile page is only accessible for the buyer who has registered the account with the website. They can assess to their own personal profile page which shows their personal information in a form, providing an option to edit their details, the order summary showing the order number. The order number is a link so the buyer can view their order detail by clicking on it. Each order number showcases the purchased date, item detail and order total. The product navigation links for the registered and non-registered shopper are the same because this is an e-commerce platform where everyone can purchase product even if they are not registered yet. Restricting the purchase ability for the registered user might affect the sales which is not ideal. 

#### *Wireframes* 
* [Profile](/design/wireframes/profile.png)

### **BLOG PAGE**
The blog section is placed below the landing image in the home page. User can view the product review by clicking on the *product review* button. The page shows the top products review chosen by the admin. The content displays the product name, description, and date posted. The *Read More* link directs the user to it's corresponding product review page [Blog Detail Page].
#### *Wireframes* 
* [Blog](/design/wireframes/blog.png)

### **BLOG DETAIL PAGE**
The blog detail page displays the product name, description, date posted, comments if anyone has done the review on that product. The comment section is showing the author, date posted and their posted review. The form below the page allow anyone to fill in their name, email, their own review on that particular product. All submitted comments will be shown in the comment section in the same page.
#### *Wireframes* 
* [Blog Detail](/design/wireframes/blog_detail.png)

### **SIGN IN PAGE**
The login page consists of the feature for the user to log in by entering the correct username/email and password. Once the user key in the correct input field which matched to the database, it will then redirect the user to the user's profile page. A *Sign Up* link is displayed above the form for the user to create an account. User can reset their password by clicking on *Forget password* link below the form in case if they have forgotten their password or for any security reason.    
#### *Wireframes* 
* [Sign In](/design/wireframes/sign_in.png)

### **SIGN UP PAGE**
The sign up page consists of the feature for the user to create their username, email and password. Once the user has created their username and password, it will then redirect the user to the home page.
* [Sign Up](/design/wireframes/sign_up.png)

### **PRODUCT MANAGEMENT PAGE**
The product management page allows the admin to add new product to the store. The form contains the options of category, sku, product name, product description, volume if available, price and rating. Admin can upload the product image as well. This page offers an easy accessibility for the admin to manage their product. 
![Sign Up](/design/screenshot/product_management.png)

# Future Features to Implement
### **Product Inventory Management**
* Planned feature: The quantity of the products are adjusted automatically once the purchase has been done on it. This can enhance the business effectiveness and in turn boost the sales.
* Inventory level visualization for non-registered user, registered user, and admin. 

### **Top Product List Banner**
* Planned feature: The top selling products will show up as an animation banner in the home page where the database will acknowledge the product selling information details in terms of their selling quantity.  

### **Product order back-end reporting**
* Planned feature: Product ordering by selling date.
* Planned feature: Product selling quantity data.
* Planned feature: Provide CSV download for business analysis.

### **Admin and Content Management**
* Planned feature: Adding and deleting category through a front end route. Currently only possible to add through the admin panel.
* Planned feature: Adding and deleting blog post through a front end route. Currently only possible to add through the admin panel.

# Defensive Programming
* Unauthorised access: 
    * Users are only presented with links they are authorised to access in the front-end.
    * The back-end blocks access to unauthorised users via decorator function. For example a registered or non-registered user are trying to access the admin page by adding */admin* in the url, user is directed to the django login page and require to type in the username and password. 

* Invalid product quantity input:
    * Users are only able to select positive numbers in the quantity input in the product page and cart page. An invalid negative number will throw and error message *Value must be greater than or equal to 1*. No further action will be process till a valid quantity number is exist in the quantity input box.

* Invalid card details input to the payment form:
    * Users can only key in the valid card details. Invalid card details will inhibit the users to proceed. An error message will be shown as *Your card number is invalid*. This prevent any users trying to bypass the payment check by using any invalid card details.

# Technologies Used

## LANGUAGES
* [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5) - For building the web structure.
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS) - For specifying how documents are presented to users.
* [Javascript](https://www.javascript.com/) - A dynamic computer programming language commonly used as a part of web pages.
* [Python](https://www.python.org/) - Programming used for this full stack project.
* [Django Templating Language](https://docs.djangoproject.com/en/3.2/ref/templates/language/) - Used to generate HTML from site template.

## DATABASE
* [Postgres](https://www.postgresql.org/) - A powerful, open source object-relational database system.
* [Sqlite3](https://www.sqlite.org/index.html) - A C-language library that implements a SQL database engine.

## LIBRARIES
* [Django](https://www.djangoproject.com/) - Python-based open-source web framework, which follows the model-template-view architectural pattern.
* [Bootstrap](https://getbootstrap.com/) - Framework for building responsive, mobile-first websites.
* [Jquery](https://jquery.com/) - Use to simplify DOM manipulation.
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library.

## PLATFORM
* [Heroku](https://www.heroku.com/) - For hosting project.
* [Amazon S3](https://aws.amazon.com/free/) - Used to store site static and media files.
* [GitPod](https://www.gitpod.io/) - Online IDE for project development. 
* [GitHub](https://github.com/) - For storing project remotely.

## Tools
* [Git](https://git-scm.com/) - For version control.
* [Am I Responsive](http://ami.responsivedesign.is/) - For checking page responsiveness and readme content.
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) A built-in web developer tools for Google Chrome Browser.
* [PIP](https://pip.pypa.io/en/stable/installation/) - For installing essential tools.
* [Stripe](https://stripe.com/) - A powerful and flexible tools for internet commerce.

## EDITORS
* [LucidChart](https://lucid.app/documents#/dashboard) - Used to create Entity Relationship Diagrams of the database.

* [ResizeImage](https://resizeimage.net/) - For resizing images.

## OTHERS
* [FontAwesome](https://fontawesome.com/) - Font and icon toolkit.
* [Gitignore](https://www.toptal.com/developers/gitignore) - Font and icon toolkit.
* [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX.
* [Slack](https://app.slack.com/client/T0L30B202) - A collaboration hub that connects your organization.

# Deployment
## To run the application on your local PC / Local Deployment
This project was performed on a Window PC. The following instruction might varied slighly on a MAC OS. 
1. Direct yourself to [The Grind House Github repository](https://github.com/kenweechin/the_grind_house).
2. Find the *Code* dropdown button and click on *Download ZIP* option, this will lead to a files extraction to your desktop/laptop environment. The other method is to clone the project by running this command on your terminal: `git clone https://github.com/<username>/<repository>`
3. Use the following command `pip3 install -r requirements.txt` to install all the essential packages.

## Database Deployment
Migration is the process where Django sets up the database. To update the database from the project root to the latest models, 
1. Generate the python migration command: `python3 manage.py makemigrations`
2. Run the command `python3 manage.py migrate` the database will begin to update.

## Python Environment 
Python environment need to be set up after repository cloning. Ensure python3 is installed. 

## Environment Variable
Required variables:
* SECRET_KEY
    * Defines Django secret key. New keys generation can be done by running this command `python3 gen_secret_key.py` from the project root.
* DEFAULT_FROM_EMAIL
    * Defines a test email account.
* DEVELOPMENT
    * If set the project to debug mode.
* EMAIL_HOST
    * The smtp address of the email service provider.
* EMAIL_HOST_USER
    * Email username
* EMAIL_HOST_PASSWORD
    * Email password
* DATABASE_URL
    * The URL of the remote database
* USE_AWS
    * Amazon S3 will be used for static and media file storage.

The following variables are essential for Amazon S3 variables:
* AWS_STORAGE_BUCKET_NAME
* AWS_S3_REGION_NAME 
* AWS_ACCESS_KEY_ID 
* AWS_SECRET_ACCESS_KEY 

Essential Stripe payment variables:
* STRIPE_PUBLIC_KEY  
* STRIPE_SECRET_KEY 
* STRIPE_WH_SECRET  

**Remote Deployment**
The site is deployed to Heroku app at: https://kenweechin-the-grind-house.herokuapp.com/
 














