# Final Landmark Assignment Django Full Stack

## Robin Collins

## The Horseshoe Inn

## Project Purpose

This is a real pub my friend Paul and his partner Toni purchased on 2nd June and moved in on 16th July 2020 amid a pandemic.
This is a genuine requested website and will be used once submitted for assessment and I am aware
that I will require to use a branch should any urgent updates be required.

With all the drama good and bad, Paul and Toni have experienced along the way, they have gained media attention
from Channel 5 who are now making a documentary of the pub. Paul and I had discussed this landmark assignment could 
potentially give my career some exposure at the same time freeing his time on people wanting to book rooms and view
constantly updated menu items. 

I, therefore need to call on all my strengths and work hard on my weakness in delivering a high scoring assignment 
that I can and just as importantly provide to my friends that can use to benefit and give them back valuable time out of 
their business with the power of a funtional website.

If the documentary proves popular, The Horseshoe Inn will require a fresh, and inviting website that is not over
complicated and easy to navigate with a secure but easy booking system. Which provides a secure account to the customer
to update their booking. Obviously, I have to also protect the client as well as a late cancellation will cause financial 
issues so deposits of the percentage of costs will have to be deducted from late cancellations for example. I also have to 
be aware of stock control as there are only 5 rooms and self-catering outbuilding that requires to only be available once 
during a day between for instance 2 pm until 10:30 pm the following day. Early cancellation will be refunded with bookings
cancelled within 48 hours will lose a deposit and 24 hours full amount.

The Additional information such as a Menu page and what to do in the area may appeal to the visitor to stay longer benefiting
the establishment.

As you are aware the hospitality industry has suffered like many individuals and businesses in 2020 and needs a boost. 
With the issues of 2020, this will also require and have key Information of updates to current rules and regulating and a website with social media links where immediate update are not
possible on the website.

I'd like to think that this website is helping a community and repair the tourism and hospitality sector that has suffered
possibly irreparable damage in 2020 in the UK with thousands of closures and job losses.


## UX design

A room booking system is the main requirement, with easy date select and checkout with the option to add extras.
For instance: breakfast. By having the option to register will allow the Inn to have a database of guests. therefore
with a checkbox on registration they can recieve quarterly/monthly newsletters or be informed of last-minute room
availability.

## Wireframes

Home & Menu

![Wireframe Home Menu](horseshoe_inn/mockup_images/horseshoe_1.png)

Rooms & Romms Scrolled down

![Wireframe Rooms](horseshoe_inn/mockup_images/horseshoe_2.png)

Room with room selected & Date Booking Select

![Wireframe Room with Select Room](horseshoe_inn/mockup_images/horseshoe_3.png)

Room enter details booking with payment & Booking Confirmation

![Wireframe Booking and Payment](horseshoe_inn/mockup_images/horseshoe_4.png)

Contact page & Respose to webform message page

![Wireframe Contact and Response](horseshoe_inn/mockup_images/horseshoe_5.png)

Terms & Conditions and a Covid-19 public information for rules and regulations

![Wireframe Terms and conditions](horseshoe_inn/mockup_images/horseshoe_6.png)

## User Stories

![userstories](horseshoe_inn/mockup_images/userstories.png)

## Usability and Visual Impact:

The website is easy to navigate with an emphasis on colours similar to the colour pallet of the public house to keep
continuity and branding. The colours are also associated with that of nature and escapism. In my research, I what
I had in mind is relevant to other public houses. 

## Suitability for purpose

This has purpose as my friend and client needs this almost immediately however there are still are technical issues
move advanced than me and an alternate short term solution will be set up during the assessment on this assignment.
However, I will be coming back to this as a lot of information and media requested hasn't been forwarded due to the
clients workload.

## Navigation

The navigation is simplified with dropdown boxes to the appropriate pages with a large button to take you to the booking
area the main purpose of the website.

The Facebook link has been set up for the actual pub additional information wasn't provided.

## Ease of use

I like to think the ease of use with this website would appeal to all ages and technical abilities giving peace of mind with
a secure and professional checkout.

## Information Architecture

## Defensive Design

Using the built-in Django validation I have used this to allow me to check model and form fields. 
Price limits have been set in Stripe.
There is also a limit on image sizes should administration add a large image the CSS can adjust this accordingly
however, load times would still be an issue.

## Layout and Visual Impact:

## Responsive Design

I have as required taken the mobile-first approach as required and a common and required practice in all assignments 
throughout my course. I have relied on Bootstrap technologies to achieve this.

## Image Presentation

## Colour scheme and typography

Using google fonts and my fonts dot com. I used a picture of the front of the inn to identify
what their pub font is and the closest match that was free was Libre Baskerville.
This will keep continuity with the establishment and continue with the continuity I have
gone with their new green interior colour scheme which is #B6D7A8 the font colour for the logo font
is B2B2AB I picked this colour as a colour match from photoshop from the picture with the font.
This colour is subject to change as the image give the impression its a soft gold but I have a grey-green look.
This could be due to the current low resolution of the images. I will look again when I
take photographs later this month. What does concern me later is the possible adverse weather conditions 
to bring out the best lights but this has never been an issue before.

Originally as to familiarise myself with this assignment I am using the code institute Boutique Ado education
videos to guide me through the process and I did think the black and white colours for Font and banners went 
extremely well with the colours of the front of the pub and I didn't want to change them but glad I did as 
the softer tones feel more inviting and a lot more relaxed and in keeping with the lucious scenery and countryside
surrounding the Horseshoe Inn. It featured in my choices when discussing this project with my client in July and
it was in my mockup styles and what is even more impressive my client painted a lot of there interior with the same
colour so for continuity reasons it would be silly not to match this.

## Languages used for assignment

I used HTML, CSS, JavaScript and Python within Django . Markdown was used in this Readme document.

## Application Features:

* Home Page
* Drop down Navigation
* Date Picker/calendar
* Menu Page - featuring Starter, Mains, Dessert and Ala-Carte. The breakfast options removed.
* Contact Page - Email not included at this stage display only.
* Events Page - Incomplete due to no content provided
* All Product page - Removed to as unessarry
* Public Information Page - Featuring all Current health notices and terms and conditions - Information not provided
* Special Offers - Incomplete due to the same reasons.
* Accommadation - Showing the selection of room originally 5 dropped to 4 as required for friends and family. allowing
for booking and taking information from the booking and secure payments. Confirmation emails are also part of this function.
* Focus is as a mobile first Application

## E-commerce

For this I used stripe adding Secret key, public keys and webhooks.

## Authentication and Security

## Software Development practices:

## Directory Structure and File Naming

## Version control

For this I used Github as advised by the Code institute - unfortunately, I did have a few issues with my original work
suffering a catastrophic error so I had to create a new branch. Fortunately, I didn't lose anything but I believe this a 
result of clearing my cache and cookies to get function back into my website when there had been errors with certain 
functions. 

I have now set the function to push to Heroku at the same time now which is extremely convenient.

## Testing write-up

## Technologies Used

* Django - https://www.djangoproject.com/ The Python Web framework used for full stack assignemt.
* Github - https://github.com/ Where I stored my assignment.
* GitPod - https://www.gitpod.io/ This is the developer used for the assignment.
* Heroku - https://www.heroku.com/ The assingnment is hosted here as Python friendly.
* Bootstrap - https://getbootstrap.com/ to aid with responsive development.
* mdbootstrap - https://mdbootstrap.com/docs/jquery/navigation/footer/
* Google Fonts - https://fonts.google.com/ The Fonts used for The Pubs main title.
* What the font - https://www.myfonts.com/WhatTheFont/ I used this website to identify the Font Used on the fron of the pub.
* Json Formatter - https://jsonformatter.org/ For improving script layout.
* Code Pen - https://codepen.io/ I used this to practise snippets of code.
* Repl.it - https://repl.it/ I also used this for seeing if snippets of code would work.
* Django Key Generator - https://miniwebtool.com/ To renew SECRET_KEYS for greater security.
* Unsplash - https://unsplash.com/ I used this to provide stock images when testing.
* Photoshop - https://www.adobe.com/uk/products/photoshop.html  Used for The Horseshoe Inn Logo Design and the Favicon.
* Balsamiq - https://balsamiq.com/ Used for the wireframes seen earlier in the project.
* Stripe - https://stripe.com/en-gb Secure Payment System.
* AWS S3 Bucket - https://aws.amazon.com/s3/ for storage of data and images in database.
* Pillow - https://pypi.org/project/Pillow/2.2.1/ links images to the database.
* PIP - https://pip.pypa.io/en/stable/ - Package management system.
* Crispy Forms by Django - https://django-crispy-forms.readthedocs.io/en/latest/
* Allauth by Djang - https://django-allauth.readthedocs.io/en/latest/
* S3transfer https://pypi.org/project/s3transfer
* Gunicorn https://gunicorn.org/ allows deployment to Heroku from Django
* Boto3 https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
* Gmail - https://mail.google.com/ popular versatile and flexible email provider
* Psycopg2 - https://pypi.org/project/psycopg2/ A postgresSQ database for Python
* AWS S3 Bucket - https://aws.amazon.com/s3/ Amazon file to store static file and images to a database
* Django Storages - https://django-storages.readthedocs.io/en/latest/
* DJ_Database - https://pypi.org/project/dj-database-url/
* Atom https://atom.io/ 


## Comments and Diary

In the early stages of development, I was having linking issues with the Readme file. Basically, I wanted
the best assignment possible with the best readme, therefore, wanted to add images to the readme rather
than have them stored in a Wireframes folder. I had been shown how impressive some of these files are
and it left me inspired.

It is something I hadn't learned on the course so decided to research into this and successfully found
videos of this on YouTube. However, I think the video was slightly dated and got a few errors with the
links not working correctly and I decided to edit within Github rather than GitPod. This was something
I hadn't done before so I did make 2 or 3 commit errors by not adding a comment in the box at the bottom
of the page and the preview option until my 4th attempt.

I contacted tutor support as concerned these errors would go against me hence I am documenting them
now to make the assessor aware of my errors which I can say have now been resolved. Despite all of this I
found it a great learning curb as worked out alternate ways to update and alter using git commands and
editing from Github directly.

In week two of development, my friend sent me images of The Horseshoe Inn since it had been refurbished
however these images I received were very small images suitable for smaller devices but not the large
screens. However, due to his workload, he has been unable to get the images to me and further deadlines
get missed due to how busy he is that after a week I have decided to continue with image placers that
fill the gaps until he has time to fulfil my request. I am due to visit in late October 2020 but feel that
this assignment needs to be completed before then as good practice for the industry.

Furthermore, while working on this assignment I have also undertaken the task of building another Django 
website for another customer my niece for her vegan cake shop Vixen's Vegan Delights. I did this as I 
knew the amount of pressure my friend is under buying a pub during a pandemic and making it work knowing 
potentially it could go very wrong. To assist him I have plenty of ideas to support him on the way to his
and my successes.

02/10/20

I have found out my deadlines and after a chat with my mentor, he has advised me not to take on the huge
task of simultaneously building 2 large websites as just one was pointed out to me by student services as
a behemoth. I have also been in contact with Paul again at The Horseshoe Inn and he agrees that the
workload for both of us is vast. This project will remain the priority and I will continue with 
Vixen's Vegan Delights after I am closer in completing this assignment.
Furthermore, I am due to travel back to Scotland for further meetings and include terms and conditions
and take professional pictures of the establishment. My cut off day for the assignment is 16th December
however, I hope to submit the assignment around the 1st November to allow me to assist other customers 
and clients I have gathered.

03/11/20

With the delay in images, I took a trip to Scotland to get these images while Scotlands hospitality industry
had been closed to public houses. However, there were issues with getting these images as Paul and Toni decided
to decorate the rooms for letting. Therefore what I went there for I could not achieve. I won't lie I was disappointed
and possibly angry as this has proven expensive and time-consuming and then being overwhelmed with guilt as could have
attended my auntie and God Mothers funeral. I have to live with these decisions furthermore, I do understand Paul 
and Toni's and where there was doubt two weeks before going away maybe it should have been pushed back to a 
different time.

Before all these the Website meetings we had gone well but they decided they want a darker green colour
for the website. I had already decided that the green colour already being used wouldn't work for smaller devices
and will therefore see where I can improve this but first I need to fix the functionality of the website first.

25/11/20

The sheer size of this project has blown me away a little as my head decided it had forgotten how to do certain tasks
after a day trying to get my date picker to function. I decided I best commit my work as my eyes really were starting
to hurt even with blue light filters. However, these commits failed due to a large Microsoft file glitch was causing
this fail. Apparently, it is known of but I thought it would be a good idea to mention as once my project was committed
it went from my initial 118 commits to 225.

04/12/20

I had more issues with my repository I'm not sure if it was due to a cache issue when I had to keep clearing it when
my site kept flagging errors and clearing the cache got it functioning again. This required me to log back into all
my sites. Commit were made but today despite a branched project displaying all the correct information my original master
did not and implied I hadn't committed for 3 days which clearly wasnt the case. However, the only thing I could do was
in the terminal type: $ git checkout  then $ git pull
I made a quick adjustment to bag.html and made the commit noting this issue at the same time and everthing was successful.

07/12/20

I lost a day due to my workspace of 3 months becoming corrupted. I notified Gitpod and I am still waiting for a Response
I believe it was to committing work after my cache being cleared in the browser and logging me out of my programs.
I have now had to set a branch up and reinstall migrations. The only positive I have taken from this is I now know what
to do if this happens again.
Sadly I lost all my rooms and menu items in my database, however, I have been advised only add one or two items for testing purposes
before adding to heroku database.

13/12/20

My final diary input as I fix the problems in the terminal where I just reflect on this truly epic journey of Django.
Sadly a lot of the requirements of this project as this beginning stages were no longer require in the website for example
adding breakfast to the room as due to work-load and constraints due to the COVID-19 pandemic Paul & Toni wouldn't be 
offering breakfast but that's not to say they wouldn't in future so therefore I kept those functions in for now.

I have also left the products in to show how much work I did with this assignment and commented out the navigation as to
show what I had done.

On the final stages, I checked my website for code errors long lines, for example, however, when testing the code using
pep8 online I would fix the code issues, however, when putting it into practise it would flag up syntax errors. Therefore
code that hasn't been amended is solely due to this and doesn't reflect the time put into fixing these issues when using
single quotations and parentheses.

## Data store integration

## Deployment write-up Deployment write-up

I took the following steps to deploy my website to Heroku:

* Log in to Heroku and click new app.
* Name the app in lower case letters and dashes only and select the nearest location mine being Europe.
* If the name is available proceed.
* Click on the resources tab and select search and type Postgres for the Heroku Database.
* Back in the Gitpod terminal install  dj_database_url with the pip3 install command.
* Then do the same with psycopg2-binary.
* Now Freeze the requirements.
* I made sure all my requirement.txt was updated.
* I then adjusted the setting for the Database in settings.py for testing.
* Now Back in the terminal I typed the following python3 manage.py showmigrations
* I then proceeded to type python3 manage.py migrate
* I then set up myself a superuser
* An if statement was added to the database then:
* pip3 install gunicorn
* Now I created a new Procfile making sure the name matched my main workspace folder name.
* I now logged into Heroku via the terminal with the following:
* heroku login -i 
* followed by the next command:
* heroku config:set DISABLE_COLLLECTSTATIC=1 --app (my app name here)
* I then went to AWS and accessed the console selectin IAM as choice.
* In AWS in the search bar I typed in S3 and clicked on S3 cloud service.
* Then clicked creat bucket naming the same as my Heroku app.
* I select the nearest region to me unchecking block public access and acknowledged that bucket will go public.
* I then turned on the static website hosting on clicking on my bucket. Added index.html and error.html where prompted.
* Clicked on the permissions tab and then pasted in code from the CORS (Cross origin Resorce Sharing).
* Select Bucket Policy then policy generator so as to create a security policy.
* Policy type is S3 Bucket Policy
* Allow all policies by adding * to the box, Action is get object.
* From the previous tab still open from when opening the policy generator.
* Now copy the bucket ARN (Amazon Resorce Name) then paste it at the bottom of the policy generator where prompted.
* Click add statement then generate the policy.
* Copy the Json Code in the document and paste in bucket policy editor.
* Before saving add a */ within the quotations after the project name.
* Click Save
* Now scroll down to access control list and click edit.
* Check the list box for Everyone (Public Access) then click the box stating you understand the effects of the changes
made on the objects and buckets.
* Save again
* I now click sevices link. 
* Select set group name and add name - again I made this simple and similar to previous names
* Now click next step twice and create the group
* The click policy then policies and select the Json tab.
* Then click import managed policy from the pre build amazon policies.
* Use the filter search and type S3 and import the AmazonS3Fullaccess Policy.
* Using the Bucket ARN from the previous created bucket policy page in S3.
* Copy and paste it in the Json code on the line with resources as follows:
line 7, "resources": [
line 8, "arn:information goes here",
line 9, "arn:information goes here/*"
line 10, ]
* Click review policy
* Give it a name and a description I added -policy after the title.
* Click Create policy then groups select the one just made followed by permissions.
* Then attach policy
* search for policy just created and select it and click attach policy.
* Now create a user to put in the group, so click users on the far left side of the panel.
* Then add user
* Add username (your project name)-staticfiles-user.
* Allow programmatic access
* Then select next
* Now click Appropriate policy then click the next:tag then next:review
* Then click create user
* Now download the  .CSV file
* IMPORTANT to download and save as cannot do this again.
* Then close the window
* At this stage add the AWS instructions to the settings.py page
* After deploying to Heroku and Github with push command simultaneously.
* Click on the bucket in S3
* Within the object tab next to the word lits version click the refresh button and the static file will appear.
* Add the cache control statement that can be seen in settings.py
* Now goto S3 and on the bucket overview click create folder and call it media and click create folder.
* Now click on that folder 
* Inside click upload and add files.


## Stretch Goals - things to add in future.

* Ideally, I would like a better function to the booking calendar/date picker where if it is booked already it would be highlighted
red and show green if available.

* Another feature that would be nice on the individual rooms have a carousel/slide show that shows different images of the rooms.

* A cookie consent form is something that is required.

* Another Idea would be to have the login function only feature on the Menu or/and the just the rooms page.

* Another feature would be to have a different home page of portrait orientation for the mobile version of the website.
as the page reduced in size a different image would be more suitable.

* Due to an issue in my code confusing myself I have had to remove the function of + and - from the shop basket and keep the remove
option and keep a simple back button to adjust booking. I did originally have this function working but made changes
without giving myself enough notes to see what I had done. However, justifying this works as a majority of hospitality websites
do just have a back adjust booking button.

I would definitely like to link the social media aspect to this project giving the customer a greater sense of trust
and security.

There is a lot of images with this project and that is because I wanted to showcase other views of the pub.

## Submission Information

Post submitting this assignment all my superuser information will be sent to the Code Institute to assess the websites
function of add, edit and delete as suggested in the requirements.

## Media

Photographs of the Horseshoe inn are credited to myself, Robin Collins. Paul Foot the owner is also responsible for Additional
pub images. He also has the rights to the older images supplied by the previous owners therefore I thank them and the customers
of Bridgend, Kilmichael Glassary. However, these images have only been used for testing purposes and I had no intention of using
them as I mentioned earlier I did travel to take the photographs but denied.

I also have used Unsplash stock library due to not being supplied content as requested these go to:

Sebastian Coman Photography for the images with the Mozzarela and Tomatoes and the Scallop with Black Pudding.
Krisztina Papp for the Ice Cream Photograph.
Claudia Crespo - Chocolate mouse with a cherry image.
Max Nayman for what I have called - Apple and Hazelnut pie. 
Louis Hansel - the prawn curry.
Edward Franklin - Burger and fries.
Tim Toomey - Steak and Chips.
Vivian Rishe - Tray of Oysters.
Wang Xi - Lobster Platter.
Annastasiia Rusaeva - Waffels with fuit compot.

I did consider using stock images to make up for the fact I couldn't get any from the amount of time effort and money I put
into this. However, I didn't as finding free exterior pub shots is extremely difficult on free stock site producing zero results
at the time of posting this.

## Used to help 

I used the following places for sources of information and snippets of code to help me obtain my goals:

* https://www.codesdope.com/ for CSS tips

* https://validator.w3.org/ for checking my HTML

* http://pep8online.com/ to help validate my Python

* https://miniwebtool.com/django-secret-key-generator/ to generate new secret key

* https://stackoverflow.com/ always good for reference

* https://css-tricks.com/snippets/css/css-triangle/ for the CSS up arrow

* http://pep8online.com/ for checking Phython Code 


## Credits and Acknowledgements

I would like to express my eternal gratitude to Brian Macharia for being a great mentor and advisor for this and
my previous assignments. I hope our paths cross again it has been a true honour to be your padawan.

Thank you to Johann Alberts bravoalpha79 and Tim Nelson at the Code Institute for allowing me to have a greater understanding of Models
and Views with this milestone assignment.

Also thank you to all the Tutors at the Code Institute for your assistance over the past year.

Further thank goes to ckz8780 for his amazing Django lessons with the code institute which was essential refernce material.

Finally, I like to thank my supportive family In what can be described as a difficult you for the whole world.

A final thank you go to Paul and Toni for believing in me regarding this project. This is still only the beginning!
