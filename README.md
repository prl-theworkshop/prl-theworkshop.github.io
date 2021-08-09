# Bridging the Gap Between AI Planning and Reinforcement Learning (PRL) – [Workshop at ICAPS 2021 (August 5-6)](https://icaps21.icaps-conference.org/workshops/PRL/)

### This site presents the most up-to-date information about the workshop. Please, visit [ICAPS 2021](https://icaps21.icaps-conference.org/) for more general information.

While AI Planning and Reinforcement Learning communities focus on similar sequential decision-making problems, these communities remain somewhat unaware of each other on specific problems, techniques, methodologies, and evaluation.

This workshop aims to encourage discussion and collaboration between the researchers in the fields of AI planning and reinforcement learning. We aim to bridge the gap between the two communities, facilitate the discussion of differences and similarities in existing techniques, and encourage collaboration across the fields. We solicit interest from AI researchers that work in the intersection of planning and reinforcement learning, in particular, those that focus on intelligent decision making. As such, the joint workshop program is an excellent opportunity to gather a large and diverse group of interested researchers.

## Topics

The workshop solicits work at the intersection of the fields of reinforcement learning and planning. We also solicit work solely in one area that can influence advances in the other so long as the connections are clearly articulated in the submission.

Submissions are invited for topics on, but not limited to:

- Reinforcement learning (model-based, Bayesian, deep, etc.)
- Model representation and learning for planning
- Planning using approximated/uncertain (learned) models
- Monte Carlo planning
- Learning search heuristics for planner guidance
- Theoretical aspects of planning and reinforcement learning
- Reinforcement Learning and planning competition(s)
- Multi-agent planning and learning
- Applications of both reinforcement learning and planning

## Invited Speakers

[Videos of the invited talks](https://youtube.com/playlist?list=PL92l-Yigsz0tfBoq94xFSgRuHNsweeEeh) – to be released soon.

- [Danijar Hafner](https://danijar.com) - "General Infomax Agents through World Models"
	- Abstract: Deep reinforcement learning has enabled machines to solve complex control problems directly from high-dimensional camera inputs. However, these systems rely on carefully designed reward functions for specific tasks. On the other hand, humans learn about the world and perform complex behaviors without any external reward signal. In the first part of the talk, we categorize the space of possible objective functions for embodied agents. We show a spectrum that reaches from narrow to general objectives. While the narrow objectives correspond to external rewards as typically used in reinforcement learning today, the general objectives correspond to information maximization through world models. This explains unsupervised learning, perception, exploration, skill discovery, and control from a single principle. The second part of the talk highlights the progress we have made in implementing such general agents, from learning world models for planning from pixels to model-based skill discovery and planning to explore.
- [Aviv Tamar](https://avivt.github.io/avivt/) – "Learning to Plan and Planning to Learn"
	- Abstract: Two main paradigms for solving sequential decision making problems are planning - searching through possible future outcomes to achieve a goal, and reinforcement learning (RL) - learning reactive policies through trial and error. This talk focuses on algorithmic interfaces between planning and RL. We start by asking about the capability of deep networks to learn planning computations, and present the Value Iteration Network, a type of differentiable planner that can be used within model-free RL. Planning problems, however, are goal based, and a planner must provide a solution for every possible goal. Standard RL, on the other hand, is based on a single goal formulation (the reward function), and making RL work in a multi-goal setting is challenging. We introduce Sub-Goal Trees (SGTs) - a new RL formulation based on a different first principle - the all-pairs shortest path problem on graphs. We show that for deterministic multi-goal problems, SGTs are provably better at handling approximation errors than conventional RL (O(NlogN) vs. O(N^2)), and we demonstrate empirical results on learning motion planning for a 7 DoF robot using deep neural networks. Finally, we ask how an RL agent can plan to best explore/exploit its environment, as cast in the following problem: given the training logs of N conventional RL agents, trained on N different tasks, train an agent that can quickly maximize reward in a new, unseen task from the same task distribution. We take a Bayesian RL view, and seek to learn a Bayes-optimal policy from the offline data. However, the offline nature of the problem entails identifiability challenges, for which we propose several solutions and a practical algorithm. On a range of challenging tasks, we demonstrate learning of near-optimal exploration/exploitation behavior. Remarkably, the learned behavior can be qualitatively different from the behavior of any RL agent in the data.
- [Emma Brunskill](https://cs.stanford.edu/people/ebrun/) – "Careful Pessimism"
   - Abstract: There is significant potential to better leverage historical data to improve future decision making, as in offline batch reinforcement learning. Pessimism with respect to quantified uncertainty has received significant recent interest in offline batch RL methods. I’ll present some of our recent work in this direction including pessimistic Bellman backup planning.
- [André Barreto](https://www.lncc.br/~amsb/) – "The value equivalence principle for model-based reinforcement learning"
	- Abstract: It has long been argued that, in order for reinforcement learning agents to solve truly complex tasks, they must build a model of the environment that allows for counterfactual reasoning. Since representing the world in all its complexity is a hopeless endeavor, especially under capacity constraints, the agent must be able to ignore aspects of the environment that are irrelevant for its purposes. This is the premise behind the value equivalence principle, which provides a formalism for focusing on the aspects of the environment that are crucial for value-based planning. In this talk I will introduce the value equivalence principle, describe some of its theoretical properties, and discuss how it can be applied in practice. I will also show experiments comparing value equivalence with more conventional model-learning techniques.
- [Elias Bareinboim](https://causalai.net) – "Towards Causal Reinforcement Learning"

## Schedule – confirmed

The event will be fully virtual, consisting of:

* Invited talks. 30m + 10m for Q&A.
* Oral presentations for some papers. 8m + 2m for Q&A.
* One poster session. 60m.
* Discussion sessions. 20m.

The workshop program spans two days, August 5 and 6.

* [Starts at 14h GMT, 10h EST, 16h Central European time (CEST)](https://www.timeanddate.com/worldclock/meetingdetails.html?year=2021&month=8&day=5&hour=14&min=0&sec=0&p1=57&p2=248&p3=44&p4=676&p5=37&p6=136&p7=179&p8=24&p9=224).
* [Finishes at 19h GMT, 15h EST, 21h Central European time (CEST)](https://www.timeanddate.com/worldclock/meetingdetails.html?year=2021&month=8&day=4&hour=19&min=0&sec=0&p1=57&p2=248&p3=44&p4=676&p5=37&p6=136&p7=179&p8=24&p9=224).
* [Time conversion table](https://www.timeanddate.com/worldclock/meetingtime.html?iso=20210805&p1=57&p2=248&p3=44&p4=676&p5=37&p6=136&p7=179&p8=24&p9=224).

### Thursday, August 5.

[Videos of the contributed talks](https://youtube.com/playlist?list=PL92l-Yigsz0u0AtRr67QJ-8gcnReGgzfw)

| Time (EST) | | Title |
| :---: | -------------------- | ------------- |
| 10:00  | Invited Talk | [Danijar Hafner](https://danijar.com). <em>General Infomax Agents through World Models</em> |
| 10:40  | Contributed talk | AI Planning Annotation in Reinforcement Learning: Options and Beyond  |
| 10:50  | Contributed talk | Efficient PAC Reinforcement Learning in Regular Decision Processes |
| 11:00  | Break | |
| 11:15  | Invited Talk | [Aviv Tamar](https://avivt.github.io/avivt/). <em>Learning to Plan and Planning to Learn</em> |
| 11:55  |	Discussion Session | Abstractions in Planning & RL |
| 12:15  |	Posters  | Gather.town |
| 13:15  |	Break  | |
| 13:30  |	Invited Talk | [Emma Brunskill](https://cs.stanford.edu/people/ebrun/). <em>Careful Pessimism</em>|
| 14:10  |	Contributed talk | Extending Graph Neural Networks for Generalized Stochastic Planning |
| 14:20  |	Contributed talk | First-Order Function Approximation for Transfer Learning in Relational MDPs |
| 14:30  |	Contributed talk | RePReL : Integrating Relational Planning and Reinforcement Learning for Effective Abstraction |
| 14:40  |	Discussion Session | Safe, Risk-sensitive, and Robust Planning and RL |
| 15:00 | End of day | |


### Friday, August 6.

[Videos of the contributed talks](https://youtube.com/playlist?list=PL92l-Yigsz0u0AtRr67QJ-8gcnReGgzfw)

| Time (EST) | | Title |
| :---: | -------------------- | ------------- |
| 10:00 | Invited Talk | [André Barreto](https://www.lncc.br/~amsb/). <em>The value equivalence principle for model-based reinforcement learning</em> |
| 10:40 | Contributed talk | Reinforcement Learning for Classical Planning: Viewing Heuristics as Dense Reward Generators |
| 10:50 | Contributed talk | Domain-independent reward machines for modular integration of planning and learning |
| 11:00 | Contributed talk | Neural Network Heuristic Functions for Classical Planning : Reinforcement Learning and Comparison to Other Methods |
| 11:10 | Discussion Session | Domain Generalization in Planning and RL|
| 11:30 | Break | |
| 11:45 | Invited Talk | [Elias Bareinboim](https://causalai.net). <em>Towards Causal Reinforcement Learning</em>|
| 12:25 | Contributed talk | Neural Network Action Policy Verification via Predicate Abstraction |
| 12:35 | Contributed talk | Debugging a Policy: A Framework for Automatic Action Policy Testing|
| 12:45 | Contributed talk | AlwaysSafe: Reinforcement Learning without Safety Constraint Violations during Training |
| 12:55 | Discussion Session | Next steps |
| 13:25 | Closing remarks | |
| 13:30 | (Optional) | Break |
| 13:45 | (Optional) | Additional Poster session |
| 14:30 | (Optional) | End of day |


## Accepted submissions: papers and poster #

* The numbers below will be used for indicating the spot during the poster session. (Authors, they are different from the EasyChair ID).
* Some papers will no participate in the poster session, so they do no have a corresponding poster.

[Videos of the contributed talks](https://youtube.com/playlist?list=PL92l-Yigsz0u0AtRr67QJ-8gcnReGgzfw)

Accepted submissions

* #1: Efficient PAC Reinforcement Learning in Regular Decision Processes (Alessandro Ronca and Giuseppe De Giacomo) ([Paper PDF](prl2021/papers/PRL2021_paper_37.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_37.pdf))
* #2: Predictive Control Using Learned State Space Models via Rolling Horizon Evolution (Alvaro Ovalle and Simon Lucas) ([Paper PDF](prl2021/papers/PRL2021_paper_17.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_17.pdf))
* #3: Discount Factor Estimation in a Model-Based Inverse Reinforcement Learning Framework (Babatunde Giwa and Chi-Guhn Lee) ([Paper PDF](prl2021/papers/PRL2021_paper_21.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_21.pdf))
* #4: Learning Search Guidance from Failures with Eliminable Edge Sets (Catherine Zeng and Tom Silver) ([Paper PDF](prl2021/papers/PRL2021_paper_10.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_10.pdf))
* #5: Reinforcement Learning for Classical Planning: Viewing Heuristics as Dense Reward Generators (Clement Gehring, Masataro Asai, Rohan Chitnis, Tom Silver, Leslie Kaelbling, Shirin Sohrabi and Michael Katz) ([Paper PDF](prl2021/papers/PRL2021_paper_26.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_26.pdf))
* #6: Open-Loop Online Planning for F1 Race Strategy Identification (Diego Piccinotti, Amarildo Likmeta, Nicolo Brunello and Marcello Restelli) ([Paper PDF](prl2021/papers/PRL2021_paper_1.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_1.pdf))
* #7: dcss ai wrapper: An API for Dungeon Crawl Stone Soup providing both Vector and Symbolic State Representations (Dustin Dannenhauer, Zohreh A. Dannenhauer, Jonathon Decker, Adam Amos-Binks, Michael Floyd and David Aha) ([Paper PDF](prl2021/papers/PRL2021_paper_24.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_24.pdf))
* #8: Learning a Symbolic Planning Domain through the Interaction with Continuous Environments (Elena Umili, Emanuele Antonioni, Francesco Riccio, Roberto Capobianco, Daniele Nardi and Giuseppe De Giacomo) ([Paper PDF](prl2021/papers/PRL2021_paper_39.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_39.pdf))
* #9: Obtaining Approximately Admissible Heuristic Functions through Deep Reinforcement Learning and A* Search (Forest Agostinelli, Stephen McAleer, Alexander Shmakov, Roy Fox, Marco Valtorta, Biplav Srivastava and Pierre Baldi) ([Paper PDF](prl2021/papers/PRL2021_paper_23.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_23.pdf))
* #10: Domain-independent reward machines for modular integration of planning and learning (Giuseppe De Giacomo, Marco Favorito, Luca Iocchi and Fabio Patrizi) ([Paper PDF](prl2021/papers/PRL2021_paper_38.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_38.pdf))
* #11: RePReL : Integrating Relational Planning and Reinforcement Learning for Effective Abstraction (Harsha Kokel, Arjun Manoharan, Sriraam Natarajan, Balaraman Ravindran and Prasad Tadepalli) ([Paper PDF](prl2021/papers/PRL2021_paper_5.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_5.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_5.pdf))
* #12: SOLO: Search Online, Learn Offline for Combinatorial Optimization Problems (Joel Oren, Chana Ross, Maksym Lefarov, Felix Richter, Ayal Taitler, Zohar Feldman Zohar Feldman, Dotan Di Castro and Christian Daniel) ([Paper PDF](prl2021/papers/PRL2021_paper_4.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_4.pdf))
* #13: First-Order Function Approximation for Transfer Learning in Relational MDPs (Jun Hao Alvin Ng and Ron Petrick) ([Paper PDF](prl2021/papers/PRL2021_paper_11.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_11.pdf))
* #14: AI Planning Annotation in Reinforcement Learning: Options and Beyond (Junkyu Lee, Michael Katz, Don Joven Agravante, Miao Liu, Tim Klinger, Murray Campbell, Shirin Sohrabi and Gerald Tesauro) ([Paper PDF](prl2021/papers/PRL2021_paper_36.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_36.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_36.pdf))
* #15: Debugging a Policy: A Framework for Automatic Action Policy Testing (Marcel Steinmetz, Timo P. Gros, Philippe Heim, Daniel Höller and Joerg Hoffmann) ([Paper PDF](prl2021/papers/PRL2021_paper_16.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_16.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_16.pdf))
* #16: Neural Network Action Policy Verification via Predicate Abstraction (Marcel Vinzent and Jörg Hoffmann) ([Paper PDF](prl2021/papers/PRL2021_paper_7.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_7.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_7.pdf))
* #17: Bounded-Suboptimal Search with Learned Heuristics (Matias Greco and Jorge A. Baier) ([Paper PDF](prl2021/papers/PRL2021_paper_33.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_33.pdf))
* #18: Scalable Risk-Sensitive Planning by Gradient Descent (Noah Patton, Jihwan Jeong, Michael Gimelfarb and Scott Sanner) ([Paper PDF](prl2021/papers/PRL2021_paper_30.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_30.pdf))
* #19: Neural Network Heuristics for Classical Planning: Reinforcement Learning and Comparison to Other Methods (Patrick Ferber, Florian Geißer, Felipe Trevizan, Malte Helmert and Joerg Hoffmann) ([Paper PDF](prl2021/papers/PRL2021_paper_20.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_20.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_20.pdf))
* #20: Can Reinforcement Learning solve the Human Allocation Problem? (Phong Nguyen) ([Paper PDF](prl2021/papers/PRL2021_paper_15.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_15.pdf))
* #21: A Reinforcement Learning Environment For Job-Shop Scheduling (Pierre Tassel, Martin Gebser and Konstantin Schekotihin) ([Paper PDF](prl2021/papers/PRL2021_paper_9.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_9.pdf))
* #22: AlwaysSafe: Reinforcement Learning without Safety Constraint Violations during Training (Extended Abstract) (Thiago D. Simão, Nils Jansen and Matthijs T. J. Spaan) ([Paper PDF](prl2021/papers/PRL2021_paper_13.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_13.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_13.pdf))
* #23: A Generic Dialog Agent for Information Retrieval Based on Automated Planning Within a Reinforcement Learning Platform (Vishal Pallagani and Biplav Srivastava) ([Paper PDF](prl2021/papers/PRL2021_paper_28.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_28.pdf))
* #24: Guiding Robot Exploration in Reinforcement Learning via Automated Planning: an Abstract (Yohei Hayamizu, Saeid Amiri, Kishan Chandan, Keiki Takadama and Shiqi Zhang) ([Paper PDF](prl2021/papers/PRL2021_paper_35.pdf)) ([Poster PDF](prl2021/posters/PRL2021_poster_35.pdf))
* #25: Extending Graph Neural Networks for Generalized Stochastic Planning (Ziqi Zhang and Florian Geißer) ([Paper PDF](prl2021/papers/PRL2021_paper_31.pdf)) ([Slides PDF](prl2021/slides/PRL2021_slides_31.pdf))

## Submission Instructions

We solicit workshop paper submissions relevant to the above call of the following types:
- Long papers — up to 8 pages + unlimited references/appendices
- Short papers — up to 4 pages + unlimited references/appendices
- Extended abstracts — up to 2 pages + unlimited references/appendices

Please format submissions in AAAI style (see instructions in the [Author Kit 2021 at AAAI, http://www.aaai.org/Publications/Templates/AuthorKit21.zip](http://www.aaai.org/Publications/Templates/AuthorKit21.zip)).

Some accepted long papers will be accepted as contributed talks. All accepted long and short papers and extended abstracts will be given a slot in the poster presentation session. Extended abstracts are intended as brief summaries of already published papers (a reference to the publication is expected), preliminary work, position papers or challenges that might help bridge the gap.

Paper submissions should be made through [EasyChair, https://easychair.org/conferences/?conf=prl2021](https://easychair.org/conferences/?conf=prl2021).

Please send your inquiries by email to the organizers at [prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com).

For up-to-date information, please visit the [PRL website, https://prl-theworkshop.github.io](https://prl-theworkshop.github.io).


## Important Dates

- Submission deadline: April 21, 2021 (PASSED)
- Notification date: May 14, 2021. (PASSED)
- Camera-ready deadline: June 25, 2021. ––extended two weeks. Upload it through [EasyChair](https://easychair.org/conferences/?conf=prl2021). (PASSED)
- Workshop date: August 5-6, 2021

The reference timezone for all deadlines is UTC-12.

## Previous Edition

[PRL @ ICAPS 2020](https://prl-theworkshop.github.io/icaps20subpages.icaps-conference.org/workshops/prl/)

## Organizers

- [Alan Fern](http://web.engr.oregonstate.edu/~afern/)
- [Vicenç Gómez](https://www.upf.edu/web/vgomez)
- [Anders Jonsson](https://www.upf.edu/web/anders-jonsson)
- [Andrey Kolobov](https://www.microsoft.com/en-us/research/people/akolobov/)
- [Hector Palacios](http://hectorpalacios.net/) – chair
- [Scott Sanner](http://d3m.mie.utoronto.ca)
