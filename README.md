<a href="https://github.com/jnbastos/jnbastos">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jnbastos/jnbastos/main/assets/header-dark.svg">
    <img alt="João Bastos, Software Engineer in backend, data and machine learning, building live sports data and analytics for Fan of the Match at PluggableAI, with his GitHub contributions over the past year." src="https://raw.githubusercontent.com/jnbastos/jnbastos/main/assets/header-light.svg" width="100%">
  </picture>
</a>

I build backend and data systems in Python, from the database schema to the dashboards people use, and I bring a mathematics background to data-heavy problems. 4+ years across product engineering and applied research.

[LinkedIn](https://linkedin.com/in/joao-bastos) · [Email](mailto:joaomnovaisbastos@gmail.com) · Braga, Portugal

## What I work on

- **Now: Software Engineer at PluggableAI.** [Fan of the Match](https://www.fanofthematch.ai) is an AI platform that reads crowd energy through fans' smartphones, used by 10+ clubs. I designed and built its live sports-data system, cut end-of-match scoring from minutes to about a second, and built the analytics and customer dashboards.
- **2024: Data and Application Engineer at DTx CoLAB.** On Be.Neutral, a national programme for carbon-neutral urban mobility, I built a base-station placement solution with clustering and optimisation, balancing coverage and cost, and backend APIs and authentication for an IoT platform for shared cars and bikes.
- **2022–2023: Research Fellow at NETEDGE**, an edge-computing project for telecom networks (below).
- **MSc in Mathematics and Computation (Machine Learning)**, University of Minho, dissertation graded 19/20.

Most of my professional code is private. These are the public projects I can show.

## Selected work

### [NETEDGE MEP](https://github.com/UMinho-Netedge/netedge-mep-uminho): running apps at the edge of telecom networks

**What MEC is.** Multi-access Edge Computing (MEC) is a telecom standard from ETSI for running applications inside the operator's network, close to users, instead of in a distant data centre, so they respond faster. At its centre is the MEC platform (MEP): applications register and find services through it, and it sets up their network and DNS rules and handles their start-up and shutdown.

NETEDGE MEP is an open-source MEP built by a team from the University of Minho, Instituto de Telecomunicações and DSTelecom, and described in an [IEEE ISCC 2023 paper](https://doi.org/10.1109/ISCC58397.2023.10217942) of which I am second author.

<img src="https://raw.githubusercontent.com/jnbastos/jnbastos/main/assets/netedge_architecture.png" alt="NETEDGE MEP architecture: MEP Server and MEP Config micro-services, OAuth, MongoDB and a DNS micro-service running on Kubernetes, with applications on one side and the platform manager (MEPM) below" width="640">

<sub>Figure 1 from Ferreira, Bastos et al., IEEE ISCC 2023. © 2023 IEEE, reused by the author.</sub>

My part:

- I built the **DNS micro-service** (right of the figure), which lets users reach applications' services by name. [Code](https://github.com/UMinho-Netedge/dns_ext)
- I built the **platform manager** (MEPM, bottom), which deploys, configures and removes applications across several edge sites through the Open Source MANO orchestrator. [Code](https://github.com/UMinho-Netedge/netedge-mepm-uminho)
- I co-developed the **MEP Server and MEP Config** micro-services with the team, mainly the application start-up and termination APIs, service registration and the configuration data models. [Code](https://github.com/UMinho-Netedge/netedge-mep-uminho)

### [Household water-use patterns](https://github.com/jnbastos/household-water-use-patterns): MSc research

<a href="https://github.com/jnbastos/household-water-use-patterns"><img src="https://raw.githubusercontent.com/jnbastos/household-water-use-patterns/main/figures/daily_profiles.png" alt="Three typical daily water-use profiles found in 342 households" width="560"></a>

Grouped 342 households by how they use water through the day, using smart-meter data from Águas do Norte. Describing each home with five summary figures instead of its full 24-hour curve gave the most consistent groups, and on the largest dataset it ran about 500 times faster than the same algorithm on full curves.

[Code](https://github.com/jnbastos/household-water-use-patterns) · [Dissertation](https://repositorium.uminho.pt/entities/publication/c8ec9929-953a-4e22-a9ac-8dec8cd1a096) · [JOCLAD 2023 abstract](https://clad.pt/DOC_EVENTOS/BookofAbstracts_joclad2023.pdf#page=119)

## Tools I use most

**Backend:** Python, FastAPI, SQLAlchemy, MySQL, MongoDB, Redis, REST APIs  
**Data and ML:** pandas, NumPy, scikit-learn, time series, clustering, optimisation  
**Infrastructure:** Docker, Kubernetes, Azure, GitHub Actions, automated testing

## Publications

- Ferreira, V., **Bastos, J.**, Martins, A., Araújo, P. J., Lori, N., Faria, J., Costa, A. and Fernández López, H. (2023). [NETEDGE MEP: A CNF-based Multi-access Edge Computing Platform](https://doi.org/10.1109/ISCC58397.2023.10217942). IEEE Symposium on Computers and Communications (ISCC).
- **Bastos, J.**, Ferreira, F., Silva, D., Erlhagen, W. and Bicho, E. (2023). [Clustering analysis for household week-daily water consumption profiles characterization](https://clad.pt/DOC_EVENTOS/BookofAbstracts_joclad2023.pdf#page=119). JOCLAD 2023, oral presentation.

---

<sub>The terminal header above is drawn by a small, tested Python script ([build.py](https://github.com/jnbastos/jnbastos/blob/main/build.py)) and redrawn monthly by GitHub Actions, so the uptime and the yearly contribution count stay current.</sub>
[![Build header](https://github.com/jnbastos/jnbastos/actions/workflows/build.yml/badge.svg)](https://github.com/jnbastos/jnbastos/actions/workflows/build.yml)
