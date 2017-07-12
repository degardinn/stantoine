# Centre Saint Antoine 50+

## Existing website
The Centre Saint Antoire 50+ existing website was developed graciously, for free, by *Evolio*. It presents 
the Centre objectives and activities and is targeted at the elders, or persons looking at supporting
them. This is reflected by a smooth design with soft, bright colours, a dominant of pink, carrying a feeling 
of calm and serenity.

### Need for a new website
A few points motivate the creation of a new website:
- The Centre Saint Antoine, which was part of a bigger organization, has become autonomous and the website
doesn't reflect that
- The website information is outdated and there is no way for the Centre Saint Antoine staff to update it.
*Evolio* don't support the website anymore.
- The website is somewhat unfinished

### Improvements
A few other points would need improvement: 
- website not responsive, inadapted to mobile devices
- complex and confusing design and links
- small fonts, inadapted to visually impaired people
- doesn't respect the W3C norms, whcih means the accessibility is compromised. It may imply a bad behavior
with the browser features, with search engines, or when using assistive technologies
- free hosting if possible

## New website
A preliminary discussion with *Elise Campeau* established some important points of the new website:
- the website content must be modifiable by the Saint Antoine Centre staff
- the gifts feature (redirecting to https://www.canadahelps.org) has to be functional
- there must be a photo gallery and a newsletter section
- there must be a functional "contact us" form
- there must be a simplified version of the "apply to become a volunteer" form
- internationalization FR/EN

The initial commit contains a prototype of the new website. Everything will be subject to change, but here
are the main guidelines concerning the new website:
- responsive design using Bootstrap
- no information about the design so currently reusing the colors of the logo
- onepage site, simple navigation
- clear and readable font

## Tech
- The website makes use of **Bootstrap** to provide a reponsive base with a grid system
- **SCSS** is used to generates the *CSS* files
- A **Netbeans** project directory is set
- A **Visual Studio Code** project directory is set
- **Python** framework **Django** + **DjangoCMS**
- **jQuery** is available
- **Dockerfile** to build and run the project as a container

### DjangoCMS

/!\ **The site now relies on the Django framework and the DjangoCMS component. Consequently, the server has to run to serve files correctly (or the assets path may be incorrect: CSS, images, scripts etc...).**

#### How to run the website

1. first ensure that **Docker for Mac**/**Docker for Windows** is installed. Refer to this tool instructions in case of need to run the **Docker** commands.
2. in a terminal, in the project root directory, run the following command to build a container: `docker build -t stantoine`. It has to be done only once. The container needs to be rebuilt only if the **Python** requirements (libraries installed with `pip`) change 
3. in a terminal, run this command to start the server (under *MacOS*): `docker run -p 80:80 --rm --name stantoine -v $(pwd):/usr/src/app stantoine`
4. in a browser, access [http://localhost](http://localhost) to see the website
5. In a terminal, run this command to see the server logs: `docker logs -f stantoine`

### TODO
- Improve the website look
- Create a "our team" contact list based on the list in *Google Apps* (if feasible through the *Google API*)
- Create the "photos" section (maybe a carousel) based on the content of a *Google Drive* directory (if feasible)
- Create the "newsletter" section based on the content of a Google Drive directory (if feasible)
- create the views, along with the CMS editable fields
- connect the forms
- add everything necesary for SEO
- ensure the website passes the W3C validation
- surely other points... Wrote that a bit quickly.
- find a cheap host that supports Python 3.4 or Docker containers, and deploy the website