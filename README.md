# MapYourDegree — Built for HackBeanPot2025

## What is Map Your Degree?
### Inspiration:

As first- and second-year undergraduate students at Northeastern University, we set out to improve how students visualize and plan their academic journey—without the confusion of the Degree Audit system. Too often, this tool leaves students feeling more overwhelmed than prepared, so we wanted to create a better alternative.

Our goal was to develop a platform that makes course planning simpler, faster, and more visually intuitive. We focused on delivering a streamlined, engaging experience that presents accurate, easy-to-interpret data, helping students confidently map out their remaining coursework.

### What it does:

Map Your Degree is a user-friendly, intuitive platform designed to help students quickly understand the most efficient path to completing their degree.

The website features a Plan Your Degree page, where users can simply input the URL of their degree program. In seconds, the platform generates interactive tables displaying key academic requirements—such as Major Requirements, Supporting Courses, and Writing Requirements.

Students can then check off completed courses, and with the press of a Save button, receive visual pie charts illustrating their progress. These charts break down degree completion percentages, making it easier to track remaining requirements at a glance.

Additionally, the site includes concentration options, allowing users to explore and understand the coursework needed to fulfill specific focus areas.

With Map Your Degree, planning your academic journey has never been easier!

### How we built it:

We built Map Your Degree using Python for the backend and Streamlit and CSS for the front-end display. Throughout development, we explored multiple approaches to ensure the best possible user experience within our limited timeframe.

All data in the app is collected and processed in real-time by scraping course requirements directly from the user-provided URL, tailoring the information to each major and degree type. Streamlit played a crucial role in allowing us to efficiently present our findings, but all pages and visuals were designed entirely from scratch.

Since this was a hackathon project, we had to adapt quickly. Initially, we planned to build the website using React and Node.js, but after developing the beginnings of the HTML, CSS, and JSX, we realized that this approach would slow us down and limit the depth of our implementation.

We also experimented with storing the scraped data by converting CSV files into SQL databases and JSON, but ultimately found that analyzing the CSV directly with Pandas was the most efficient solution.

In true hackathon spirit, we embraced every unexpected twist in our development process, documenting our evolution from start to finish. You can find our React and Node.js implementation in the map-your-degree folder, and our Java and SQL work in JavaForBean.

### How to use:
Once you have cloned the repo, make sure you have Streamlit installed (`pip install streamlit`), run `streamlit run Home.py` in your terminal and you will be able to locally host the project! Grab your Northeastern University degree requirements page URL (more schools coming soon!) and explore your degree!
