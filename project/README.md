# Idea Ocean
#### Video Demo: https://youtu.be/aADwLuZpSeA
#### Description
As a UX designer, I want to create a place to store all my great project ideas in one place. So I created Idea Ocean to be a host for all my project ideas where I could search, insert, look at, and comment on my ideas. I used VueJS as my framework with Ant Design as my UI library. I used firebase and NodeJS as by backend and use npm to manage my package.

#### Technical Framework
For this project, I use VueJS as my frontend framework and used firebase as my backend + database. Using Vue as the frontend framework allows me to create simless transition between pages and enables me to create more with less code. I believe that a light backend framework make it easier to develop and FireBase is a cool technology to use. For the UI and styling components, I used AntDesign as my design framework. I also written some of my own CSS in each Vue HTML component file. I used npm as my package manager and installed the following packages:
- ant-design-vue: core reuseable UI component
- axios: HTTP/HTTPS backend request, used to communicate with FireBase
- vue: the HTML framework for building this website.

All files of the project are listed in the src folder.

VueJS provide an elegant way to do URI routing. All routing is stored in the router.js file. For global states like button click and events, I used `store.js` to store all variables.

#### Page Organization
The component folder contains the UI pieces of the website:
- Composer
    > A writing place in which you can compose your idea and submit it to the idea ocean
- Footer
    > A common footer for the entire project
- Header
    > A common header for the entire project
- IdeaCard
    > A styled card that contains all the posed ideas like sticker notes
- IndexPage
    > The page container for the index homepage
- Login
    > The login page for user login
- Register
    > The register page for user register
- Project
    > The create project page for creating project
- Search
    > The search page in which you can search for ideas

#### UI Design
For the design color of this website, I use the sea color blue as the main color in CSS. I also added a cute whale as the mascot of the website. I use card design to wrap all the ideas into boxes and added shadows and spacing to sperate the cards from the background and between each other. I also added a Google like search field that enables the user to click and search for any ideas in the page. I added some click events and hover events that reacts to user input and performs actions such as open up a pop up or dropdown.