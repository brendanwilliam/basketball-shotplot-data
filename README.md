# **NBA Play-by-Play Archive**
*An independently developed archive of all NBA play-by-play data.*

## **Introduction**
Hi! Welcome to the most complete NBA play-by-play archive. This project contains play-by-play data from nearly 40,000 NBA games from the 96-97 season until today. In this repository you will find the raw JSON play-by-play data from the NBA website, CSVs of season/player/team specific play-by-play data, and data analysis/visualizations.

Currently I'm the only one working on this project, so I'm limited to the resources of my own personal capacity. However, *I will try and provide monthly updates to stay current with the regular season.

## **Project status**
As this project is extensive, I will be providing updates in phases. *The following table will be updated as each phase is completed.*

| Status | Phase | Description |
| -------- | -------- | -------- |
| **In progress (12/7/24)** | Gather all game URLs | Get all regular season and playoff game URLs. These will be used when exporting the raw JSON data from nba.com. |
| *Not started* | Gather all play-by-play JSONs | Get all regular season and playoff JSONs. These will be used to create CSVs representing play-by-play data. |
| *Not started* | Generate play-by-play CSVs for each season | Use play-by-play JSONs to generate CSVs for every season. Since each season can contain around 600K plays, each season will be its own file to make future data analysis more manageable. |
| *Not started* | Generate CSVs for players, teams, and more | Use existing CSVs to generate smaller CSVs for the most commonly searched metadata (ie. season, team, opponent, player, etc). |
| *Not started* | Create Dash apps | Explore the data collected through Dash apps that will be available to the public. |

## **Contact**
For any questions, concerns, or requests to collaborate, please email me at brendan@roughdraftmedia.com or message me on LinkedIn at in/brendanwillkeane.