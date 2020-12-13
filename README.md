# Venus

## Presentation
Venus is an all-in-one UX analyser that scores a website on its usability.
It uses an AI that is based on machine learning models as well as in-depth analysis algorithms.

## Features

#### UX analysis

We made in-depth analysis algorithms to evaluate:

1. The consistency and clutter of a website. Our algorithms scores the website based on the number of the possible user interactions. The more interactions, the less the score. This algorithms are defined [here](https://github.com/AI4UX/2020_PoC/blob/master/back/clutter.py) and bases their score calculations on a self-generated dataset based on various sites found with google search automated queries.
2. We also analyzed the page length and the number of items shown. This KPI is important to evaluate the complexity of the website, and therefore the difficulty to get all information for the user.
3. The load speed of the website (on desktop and mobile). A slow site implies a ruined user experience. We put this metrics in the core of our analysis to evaluate the performance of the website.
4. The information ordering. We think that the more a user scrolls on your website, the less the information he encounters should be important. Important pieces of information should be placed right at the beginning of each of your website page. In order to check this, we run two checks :
     * first we analyze the header consistency of each of the website pages : if a page mixes small and big titles in an unordered way, we reduce its efficiency score. This algorithm are defined [here](https://github.com/AI4UX/2020_PoC/blob/master/back/analysis.py)
     * then we perform keywords analysis on the top part of each pages. We analyze their relevance and importance for the user. Those keywords are then displayed on the frontend of the project after the analysis. This part uses computer vision algorithms, which implementations can be found [here](https://github.com/AI4UX/2020_PoC/blob/master/back/analysis.py)


#### UI analysis

1. The visual coherence in the colors choice. Our algorithm defined [here](https://github.com/AI4UX/2020_PoC/blob/master/back/color.py) produces statistics on the most used colors and evaluates the coherence of this choice based on color complementarity.
2. The visual cluttering : based on our statistics produced on step 1, we analyse the most used colors on certain areas of the screen and determine if the website layout is not too complex and has blank space.
3. Accessibility : with those color analytics, we also check if the website is usable for all types of color-blind people. This metrics are important because they significantly impact the user experience of color-blind people. This algorithm is defined [here](https://github.com/AI4UX/2020_PoC/blob/master/back/color.py)
4. Mobile compatibility : all of our algorithms are also used on the mobile version of the website, allowing us to check its accessibility from a smartphone.


#### Security analysis

The user experience is also impacted by the security of the page, otherwise your web browser will show warnings reduce the quality of the user journey. We check the validity of the ssl certificate [here](https://github.com/AI4UX/2020_PoC/blob/master/back/analysis.py).

#### Transfer learning

Everytime someone makes a request to analyze a website, we improve our transfer learning model. The purpose of this model is to evaluate the various KPIs we currently analyze with algorithms from a simple screenshot of the website.

The more requests are made, the more our model becomes efficient in evaluating your website KPIs.

You can find the model definition [here](https://github.com/AI4UX/2020_PoC/blob/master/back/models.py).

# Try it out

## Access

A server is currently running on our end, so access is simple!

If you want to use our tool, just click [here](https://ai4ux.poc-innovation.com/)!

Or go to this link https://ai4ux.poc-innovation.com/

## Host it yourself!

Clone the repository and launch the following command from the root:
```bash
docker compose up
```
A popup should then appear.

If it doesn't, go to your [localhost:3000](http://localhost:3000) for the frontend and [localhost:5000](http://localhost:5000) for the backend.

Made with :heart: by [PoC](http://poc-innovation.com)
