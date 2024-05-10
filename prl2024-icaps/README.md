# PRL @ ICAPS 2024

[ICAPS'24](https://icaps24.icaps-conference.org/program/workshops/prl/) \
Banff, Alberta, Canada  \
Date: June 2, 2024 \
[prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com)

<!-- **Some of the accepted papers will be invited to be presented at the IJCAI edition of the workshop as well.** -->
<!-- Timo: we will need to wait whether there is an ICJAI workshop to state something like this -->
## Aim and Scope

While AI Planning and Reinforcement Learning communities focus on similar
sequential decision-making problems, these communities remain somewhat unaware
of each other on specific problems, techniques, methodologies, and evaluations.

This workshop aims to encourage discussion and collaboration between researchers in the fields of AI planning and reinforcement learning. 
We aim to bridge the gap between the two communities, facilitate the discussion of differences and similarities in existing techniques, and encourage collaboration across the fields. 
We solicit interest from AI researchers that work in the
intersection of planning and reinforcement learning, in particular, those that focus on intelligent decision-making. This is the seventh edition of the [PRL workshop series](https://prl-theworkshop.github.io/) that started at [ICAPS 2020](https://icaps20subpages.icaps-conference.org/workshops/prl/).

## Topics of Interest

We invite submissions at the intersection of AI Planning and Reinforcement Learning. The topics of interest include, but are not limited to, the following

* Reinforcement learning (model-based, Bayesian, deep, hierarchical, etc.)
* Safe RL
* Monte Carlo planning
* Model representation and learning for planning
* Planning using approximated/uncertain (learned) models
* Learning search heuristics for planner guidance
* Theoretical aspects of planning and reinforcement learning
* Action policy analysis or certification
* Reinforcement learning and planning competition(s)
* Multi-agent planning and learning
* Applications of both reinforcement learning and planning 


## Important Dates

* Paper submission deadline: ~~March 22th~~ ~~April 5th~~ April 7th, AOE (final extension)
* Paper acceptance notification: April 28th, AOE  (Decisions are out)



ICAPS will be **in-person** this year. Authors of accepted workshop papers are expected to physically attend the conference and present in person.



## Schedule



| Time (Banff) | Title |
|:------------:|:-----------|
|     8:30     | Opening Remarks          |
|     8:35     | **Keynote Felipe Trevizan:<br>The Next-Generation of Planning Heuristics: GNNs and Beyond**       |
|     9:35     | **Poster Session I**   |
|    10:00     | Coffee break |
|    10:30     | **Talk Session I**    |
|  | The Case for Developing a Foundation Model for Planning-like Tasks from Scratch. Biplav Srivastava, Vishal Pallagani. |
|  | Equivalence-Based Abstractions for Learning General Policies. Dominik Drexler, Simon Ståhlberg, Blai Bonet, Hector Geffner. |
|  | Comparing State-of-the-art Graph Neural Networks and Transformers for General Policy Learning. Nicola J. Müller, Pablo Sanchez Martin, Jörg Hoffmann, Verena Wolf, Timo P. Gros. |
|  | Automating the Generation of Prompts for LLM-based Action Choice in PDDL Planning. Katharina Stein, Daniel Fišer, Jörg Hoffmann, Alexander Koller. |
|  | Planning with Language Models Through The Lens of Efficiency. Michael Katz, Harsha Kokel, Kavitha Srinivas, Shirin Sohrabi. |
|    12:00     | Lunch    |
|    13:30     | **Keynote Forest Agostinelli:<br>Deep Reinforcement Learning and Heuristic Search Algorithms** |
|    14:30 | **Poster Session II**  |
|    15:00     | Coffee break |
|    15:30     | **Talk Session II** |
| | Exploring Simultaneity: Learning Earliest-time Semantics for Automated Planning. Ángel Aso-Mollar, Óscar Sapena, Eva Onaindia.|
| | ModelDiff: Leveraging Models for Policy Transfer with Value Lower Bounds. Xiaotian Liu, Jihwan Jeong, Ayal Taitler, Michael Gimelfarb, Scott Sanner.|
| | Beyond Training: Optimizing Reinforcement Learning Based Job Shop Scheduling Through Adaptive Action Sampling. Constantin Waubert de Puiseau, Christian Dörpelkus, Jannik Peters, Hasan Tercan, Tobias Meisen.|
| |Online Planning in MDPs with Stochastic Durative Actions. Tal Berman, Ronen Brafman, Erez Karpas.|
| | A New View on Planning in Online Reinforcement Learning. Kevin Roice, Parham Mohammad Panahi, Scott M. Jordan, Adam White, Martha White.|
|    17:00     | **Closing Remarks**    |
|    17:05     | End      |


# Program



## Keynotes 

#### I. Felipe Trevizan: The Next-Generation of Planning Heuristics: GNNs and Beyond

##### Abstract
Deep learning has been responsible for multiple recent breakthroughs, particularly in image recognition and natural language processing. In this talk, I will focus on a particular deep learning model, Graph Neural Networks (GNNs), and how they have the potential to change heuristic search in automated planning from the heuristics used to search methods. I will introduce novel graph representations designed to optimize the application of GNNs to learning both domain-specific and domain-independent heuristics. Additionally, I will present other targets that can be learnt using GNNs, such as rankings between states, and how they can be used during search. Lastly, based on theoretical insights, we present an alternative approach to GNNs using classical machine learning methods such as SVMs and Gaussian Processes for heuristic learning, offering simplicity and reduced training times.

##### Biography
Dr. Felipe Trevizan is a Senior Lecturer at the School of Computing, the Australian National University. He previously served as a Senior Research Scientist at NICTA (now Data61/CSIRO). He earned his PhD in Machine Learning from Carnegie Mellon University in 2013. His research interests lie at the intersection of Artificial Intelligence, Operations Research and Machine Learning including automated planning and scheduling, reasoning under uncertainty, heuristic search, and learning for planning. Along with colleagues and students, he is the co-recipient of the 2016 best paper award from the Transport Research Board and the best paper award at the International Conference on Automated Planning and Scheduling (ICAPS) in 2016 and 2017.


#### II. Forest Agostinelli: Deep Reinforcement Learning and Heuristic Search Algorithms

##### Abstract
 Deep reinforcement learning has been shown to be able to learn domain-specific heuristic functions in a largely domain-independent fashion. As a result, novel variations of A* search, such as batch A* search and Q* search, have been proposed to accommodate the deep neural networks that represent these heuristic functions. In this talk, I will describe how approximate value iteration can be used to learn heuristic functions to guide batch A* search, which can exploit parallelization provided by graphics processing units. Next, I will describe how Q-learning can be used to learn heuristic functions represented by deep Q-networks to guide Q* search, which exploits the structure of deep Q-networks to significantly increase speed and reduce memory during search. Finally, I will describe how model-based reinforcement learning and hindsight experience replay can be used to extend these methods to domains with unknown transition functions. I will give several examples of application domains, including the Rubik’s cube, quantum computing, and reaction mechanism pathway prediction. The code for many of these algorithms is publicly available at https://github.com/forestagostinelli/deepxube.

##### Biography
 Forest Agostinelli is an assistant professor at the University of South Carolina. His research aims to use artificial intelligence to automate the discovery of new knowledge. He looks to apply his research to fields such as puzzle solving, chemical synthesis, robotics, quantum computing, theorem proving, program synthesis, and education. He led the creation of DeepCubeA, an artificial intelligence algorithm capable of solving puzzles such as the Rubik’s cube without human guidance. DeepCubeA has since been applied to problems in quantum computing, chemical reactions, cryptography, and parking lot optimization. He earned his Ph.D. from the University of California, Irvine under the supervision of Professor Pierre Baldi. His homepage is located at https://cse.sc.edu/~foresta/.

## Talks 
Select accepted papers are given a slot in the program: 15 minutes for content + 3 minutes for questions.

## Poster session 
The program includes two poster sessions in order to have enough time for discussions. All authors are expected to participate in the poster session.


## List of Accepted Papers


* [poster] **Contextual Pre-planning on Reward Machine Abstractions for Enhanced Transfer in Deep Reinforcement Learning**	*Guy Azran, Mohamad Hosein Danesh, Stefano V Albrecht, Sarah Keren*
* [talk] **Beyond Training: Optimizing Reinforcement Learning Based Job Shop Scheduling Through Adaptive Action Sampling**	*Constantin Waubert de Puiseau, Christian Dörpelkus, Jannik Peters, Hasan Tercan, Tobias Meisen*
* [talk] **Online Planning in MDPs with Stochastic Durative Actions**	*Tal Berman, Ronen Brafman, Erez Karpas*
* [talk] **ModelDiff: Leveraging Models for Policy Transfer with Value Lower Bounds**	*Xiaotian Liu, Jihwan Jeong, Ayal Taitler, Michael Gimelfarb, Scott Sanner*
* [poster] **Solving Minecraft Tasks via Model Learning**	*Yarin Benyamin, Argaman Mordoch, Shahaf S. Shperberg, Roni Stern*
* [talk] **A New View on Planning in Online Reinforcement Learning**	*Kevin Roice, Parham Mohammad Panahi, Scott M. Jordan, Adam White, Martha White*
* [poster] **Conviction-Based Planning for Sparse Reward Reinforcement Learning Problems**	*Simon Ouellette, Eric Beaudry, Mohamed Bouguessa*
* [poster] **Q\* Search: Heuristic Search with Deep Q-Networks**	*Forest Agostinelli, Shahaf S. Shperberg, Alexander Shmakov, Stephen Marcus McAleer, Roy Fox, Pierre Baldi*
* [poster] **Finding Reaction Mechanism Pathways with Deep Reinforcement Learning and Heuristic Search**	*Rojina Panta, Mohammadamin Tavakoli, Christian Geils, Pierre Baldi, Forest Agostinelli*
* [talk] **Planning with Language Models Through The Lens of Efficiency**	*Michael Katz, Harsha Kokel, Kavitha Srinivas, Shirin Sohrabi*
* [poster] **Guiding Hiearchical Reinforcement Learning in Partially Observable Environments with AI Planning**	*Brandon Rozek, Junkyu Lee, Harsha Kokel, Michael Katz, Shirin Sohrabi*
* [poster] **Monte Carlo Tree Search for Integrated Planning, Learning, and Execution in Nondeterministic Python**	*Rich Levinson*
* [talk] **Exploring Simultaneity: Learning Earliest-time Semantics for Automated Planning**	*Ángel Aso-Mollar, Óscar Sapena, Eva Onaindia*
* [poster] **Numeric Reward Machines**	*Kristina Levina, Nikolaos Pappas, Athanasios Karapantelakis, Aneta Vulgarakis Feljan, Jendrik Seipp*
* [poster] **POSGGym: A Library for Decision-Theoretic Planning and Learning in Partially Observable, Multi-Agent Environments**	*Jonathon Schwartz, Rhys Newbury, Dana Kulic, Hanna Kurniawati*
* [talk] **The Case for Developing a Foundation Model for Planning-like Tasks from Scratch**	*Biplav Srivastava, Vishal Pallagani*
* [talk] **Equivalence-Based Abstractions for Learning General Policies**	*Dominik Drexler, Simon Ståhlberg, Blai Bonet, Hector Geffner*
* [talk] **Automating the Generation of Prompts for LLM-based Action Choice in PDDL Planning**	*Katharina Stein, Daniel Fišer, Jörg Hoffmann, Alexander Koller*
* [talk] **Comparing State-of-the-art Graph Neural Networks and Transformers for General Policy Learning**	*Nicola J. Müller, Pablo Sanchez Martin, Jörg Hoffmann, Verena Wolf, Timo P. Gros*
* [poster] **Towards Neurosymbolic RL via Inductive Learning of Answer Set Programs**	*Celeste Veronese, Daniele Meli, Alessandro Farinelli*
* [poster] **SLOPE: Search with Learned Optimal Pruning-based Expansion**	*Davor Bokan, Zlatan Ajanović, Bakir Lacevic*




## Submission Details


We solicit workshop paper submissions relevant to the above call of the following types:

 * Long papers -- up to 8 pages + unlimited references / appendices
 * Short papers -- up to 4 pages + unlimited references / appendices
 * Extended abstracts -- up to 2 pages + unlimited references/appendices 
 
Please format submissions in AAAI style (see instructions in the [Author Kit](https://aaai.org/aaai-conference/submission-instructions/)). Authors submitting papers rejected from other conferences, please ensure you do your utmost to address the comments given by the reviewers. Please do not submit papers that are already accepted for the main ICAPS conference to the workshop.


Some accepted long papers will be invited for contributed talks. All accepted papers (long as well as short) and extended abstracts will be given a slot in the poster presentation session.  Extended abstracts are intended as brief summaries of already published papers,  preliminary work, position papers, or challenges that
might help bridge the gap.

As the main purpose of this workshop is to solicit discussion, the authors are
invited to use the appendix of their submissions for that purpose.


<!-- timo: we still need to decide whether we want openreview -->
Paper submissions should be made through [OpenReview](https://openreview.net/group?id=PRL/2024/ICAPS). 

We do not insist on papers being submitted anonymously initially; this decision is left to the discretion of the author. If a paper is simultaneously being considered at a venue where anonymity is required, you have the option to submit it without author details, considering the possibility of a shared reviewer pool. However, please be aware that upon acceptance, the paper will be publicly posted on the PRL website with full author information.

<!-- ### Workshop Proceedings (optional)

TODO

### Policy on Previously Published Materials (optional) 

TODO -->

<!-- ## Workshop Committee

TODO -->

## Organizing Committee

* [Timo P. Gros](https://mosi.uni-saarland.de/people/timo/), German Research Center for Artificial Intelligence (DFKI), Saarbrücken, Germany
* [Steven James](https://sdjames.me/), University of the Witwatersrand, Johannesburg, South Africa
* [Harsha Kokel](http://harshakokel.com), IBM Research, San Jose, USA
* [Simon Ståhlberg](https://rlplab.com/simon-stahlberg/), Linköping University, Linköping, Sweden
* [Marcel Steinmetz](https://marcel-steinmetz.org), LAAS-CNRS and University of Toulouse, Toulouse, France
* [Ayal Taitler](https://sites.google.com/view/ataitler/home), University of Toronto, Toronto, Canada


Please send your inquiries to [prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com)


<!-- ### Program Committee

TODO -->

<!-- ## List of Accepted Papers

TBD -->

<!-- ## Workshop Schedule

TBD -->

< [Link to other workshops in the series](https://prl-theworkshop.github.io)

