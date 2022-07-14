# Bridging the Gap Between AI Planning and Reinforcement Learning (PRL @ IJCAI) – [Workshop at IJCAI 2022 (July 24)](https://ijcai-22.org)

### This site presents the most up-to-date information about the PRL @ IJCAI workshop. Please, visit [IJCAI 2022](https://ijcai-22.org) for information about the general conference.

While  AI  Planning and  Reinforcement  Learning  communities focus  on  similar
sequential decision-making  problems, these communities remain  somewhat unaware
of each other  on specific problems, techniques,  methodologies, and evaluation.

This  workshop  aims  to  encourage discussion  and  collaboration  between  the
researchers in the  fields of AI planning and reinforcement  learning. We aim to
bridge  the  gap between  the  two  communities,  facilitate the  discussion  of
differences and similarities in existing techniques, and encourage collaboration
across the  fields. We  solicit interest  from AI researchers  that work  in the
intersection of planning  and reinforcement learning, in  particular, those that
focus on intelligent decision making. As  such, the joint workshop program is an
excellent  opportunity  to  gather  a  large and  diverse  group  of  interested
researchers.

## Workshop topics

The  workshop solicits work at the intersection of  the fields of  reinforcement
learning  and  planning.  One example  is so-called  goal-directed reinforcement
learning,  where a  goal must be  achieved,  and no partial credit  is given for
getting  closer to the goal.  In this case,  a usual metric is  success rate. We
also solicit work solely in one area that can influence advances in the other so
long as the connections are *clearly articulated* in the submission.

Submissions are invited for topics on, but not limited to:

* Theoretical aspects of planning and reinforcement learning
* Goal-oriented sequential decision methods combining planning, RL
  or other ML methods.
* Goal-directed reinforcement learning (model-based, Bayesian, deep, etc.)
* Safe Reinforcement Learning and Planning
* Certification/analysis of learned policies/models
* Neuro-symbolic methods for RL
* Hierarchical RL and symbolic abstractions
* Compositional RL and symbolic methods
* Planning using approximated/uncertain (learned) models
* Monte Carlo Planning
* Applications of planning methods to RL
* Various levels of generalization (across goals, objects/domain, domains)
* Reinforcement Learning and planning competition(s)/benchmarks

# Important Dates

* Submission system opened: Friday, April 29th, 2022 (UTC-12 timezone)
* Submission deadline (Extended): Friday, May 20th, 2022 (UTC-12 timezone)
* Notification date: Friday, June 3rd, 2022
* Camera-ready deadline: Monday, July 11th, 2022 (UTC-12 timezone)
* Workshop date: Vienna, July 24, 2022

IJCAI will be **in-person** this year. Authors of accepted workshop papers are expected to physically attend the conference and present in person.

# Program

The event consists of:

* [Invited talks](#invited-speakers). 45 minutes content + 15 minutes for questions.
	* [Sheila McIlraith](#sheila-mcilraith) (cancelled)
	* [Giuseppe De Giacomo](#giuseppe-de-giacomo)
	* [Sriraam Natarajan](#sriraam-natarajan)
* Talks for accepted papers. 10 minutes content + 5 minutes for questions.
* Discussions: 30 minutes.

## Schedule

| Time (Vienna) | Title |
|:------------:|:-----------|
|     9:00     | Opening Remarks          |
|     9:05     | **Keynote**: [Giuseppe De Giacomo – *Deciding and Learning How to Act in Non-Markovian Settings*](#giuseppe-de-giacomo) |
|     10:05     | **Session 1**            |
|  | [*PG3: Policy-Guided Planning for Generalized Policy Generation*](papers/PRL2022_paper_1.pdf). Ryan Yang, Tom Silver, Aidan Curtis, Tomas Lozano-Perez and Leslie Kaelbling. |
|  | [*Heuristic Search Planning with Deep Neural Networks using Imitation, Attention and Curriculum Learning*](papers/PRL2022_paper_17.pdf). Leah Chrestien, Tomáš Pevný, Stefan Edelkamp and Antonín Komenda. |
|    10:35     | Coffee break |
|    11:00     | **Session 2**    |
|  | [*State Representation Learning for Goal-Conditioned Reinforcement Learning*](papers/PRL2022_paper_14.pdf). Lorenzo Steccanella and Anders Jonsson. |
|  | [*Scaling up ML-based Black-box Planning with Partial STRIPS Models*](papers/PRL2022_paper_21.pdf). Matias Greco, Álvaro Torralba, Jorge A. Baier and Hector Palacios. |
|  | [*Graph-Based Representation of Automata Cascades with an Application to Regular Decision Processes*](papers/PRL2022_paper_22.pdf). Alessandro Ronca and Giuseppe De Giacomo. |
|  | [*Relational Abstractions for Generalized Reinforcement Learning on Symbolic Problems*](papers/PRL2022_paper_8.pdf). Rushang Karia and Siddharth Srivastava. |
|    12:00     | **Discussion**  |
|    12:30     | Lunch    |
|    14:00     | **Keynote**: [Sriraam Natarajan - *Neurosymbolic learning via Integration of (Relational) Planning and (Deep) RL*](#sriraam-natarajan) |
|    15:00     | **Session 3**            |
|  | [*Exploiting Multiple Levels of Abstractions in Episodic RL via Reward Shaping*](papers/PRL2022_paper_24.pdf). Roberto Cipollone, Giuseppe De Giacomo, Marco Favorito, Luca Iocchi and Fabio Patrizi. |
|  | [*Compositional Reinforcement Learning from Logical Specifications*](papers/PRL2022_paper_27.pdf). Kishor Jothimurugan, Suguman Bansal, Osbert Bastani and Rajeev Alur. |
|    15:30     | Coffee break |
|    16:00     | **Session 4**    |
|  | [*Deep Policy Learning for Perfect Rectangle Packing*](papers/PRL2022_paper_20.pdf). Boris Doux, Satya Tamby, Benjamin Negrevergne and Tristan Cazenave. |
|  | [*Generalizing Behavior Trees and Motion-Generator (BTMG) Policy Representation for Robotic Tasks Over Scenario Parameters*](papers/PRL2022_paper_25.pdf). Faseeh Ahmad, Matthias Mayr, Elin Anna Topp, Jacek Malec and Volker Krueger. |
|  | [*Speeding-up Continual Learning through Information Gaines in Novel Experiences*](papers/PRL2022_paper_26.pdf). Pierrick Lorang, Shivam Goel, Patrik Zips, Jivko Sinapov and Matthias Scheutz. |
|  | [*An attention model for the formation of collectives in real-world domains*](papers/PRL2022_paper_16.pdf). Adrià Fenoy Barceló, Filippo Bistaffa and Alessandro Farinelli. |
|    17:00     | **Closing remarks, discussion**         |
|    17:30     | End      |

# Invited Speakers
<!-- 
## [Sheila McIlraith](https://www.cs.toronto.edu/~sheila/)

* *Title*: **Reward Machines: Formal Languages and Automata for Reinforcement Learning**
* *Abstract*: Reinforcement Learning (RL) is proving to be a powerful technique for building sequential decision making systems in cases where the complexity of the underlying environment is difficult to model. Two challenges that face RL are reward specification and sample complexity. Specification of a reward function -- a mapping from state to numeric value -- can be challenging, particularly when reward-worthy behaviour is complex and temporally extended. Further, when reward is sparse, it can require millions of exploratory episodes for an RL agent to converge to a reasonable quality policy. In this talk I'll show how formal languages and automata can be used to represent complex non-Markovian reward functions. I'll present the notion of a Reward Machine, an automata-based structure that provides a normal form representation for reward functions, exposing function structure in a manner that greatly expedites learning. Finally, I'll also show how these machines can be generated via symbolic planning or learned from data, solving (deep) RL problems that otherwise could not be solved.
* *Bio*: Sheila McIlraith is a Professor in the Department of Computer Science, University of Toronto, a Faculty Member at the Vector Institute for Artificial Intelligence, and a Canada CIFAR AI Chair. McIlraith is the author of over 100 scholarly publications in the area of knowledge representation, automated reasoning and machine learning. Her work focuses on AI sequential decision-making broadly construed, through the lens of human-compatible AI.McIlraith is an AAAI Fellow, and an ACM Fellow. She is an associate editor of the Journal of Artificial Intelligence Research (JAIR), and a past associate editor of the journal Artificial Intelligence (AIJ). McIlraith served as program co-chair of AAAI-18, KR2012, and ISWC200. McIlraith's early work on Semantic Web Services has had a notable impact. In 2011 she and her co-authors were honoured with the SWSA 10-year Award, recognizing the highest impact paper from the International Semantic Web Conference, 10 years prior. Her research has also made practical contributions to the development of next-generation NASA space systems and to emerging Web standards. -->

## [Giuseppe De Giacomo](http://www.diag.uniroma1.it//degiacom/)

* *Title*: **Deciding and Learning How to Act in Non-Markovian Settings**
* *Abstract*: Autonomy is one of the grand objectives of AI. It is concerned with building autonomous agents/robots that operate in changing, incompletely known, unpredictable environments. Autonomy requires reasoning and planning capabilities, as well as learning from experience. Many areas of AI are concerned with autonomy, including Logic in AI, Knowledge Representation and Reasoning, Planning, Sequential Decision Making (MDPs), and Reinforcement Learning. Moreover, several objectives are shared with automated synthesis and strategic reasoning in Formal Methods. In this talk, we will show how one can merge reasoning on temporal logic and reinforcement learning to build autonomous agents that can act to accomplish temporally extended tasks in unknown environments. Handling Non-Markovianity will play a central role.
* *Bio*: Giuseppe De Giacomo is a full professor in Computer Science and Engineering at University of Roma La Sapienza. His research activity has concerned theoretical, methodological and practical aspects in different areas of AI and CS, most prominently Knowledge Representation, Reasoning about Actions, Generalized Planning, Autonomous Agents, Service Composition, Business Process Modeling, Data Management and Integration. He is AAAI Fellow, ACM Fellow, and EurAI Fellow. He has got an ERC Advanced Grant for the project WhiteMech: White-box Self Programming Mechanisms (2019-2024). He has been the Program Chair of ECAI 2020.  He is on the Board of EurAI.

## [Sriraam Natarajan](https://personal.utdallas.edu/~sriraam.natarajan/)

* *Title*: **Neurosymbolic learning via Integration of (Relational) Planning and (Deep) RL**
* *Abstract*: One of the challenges in constructing a two level system, for instance, a higher-level deliberative planner with a lower level reactive RL agent, is the interface between these two systems. In this talk, I argue that this interface is crucial in constructing appropriate abstractions for the underlying RL agent to be efficient and effective. Specifically, I outline our RePReL system that constructs these abstractions automatically using a dynamic Statistical Relational Learning (SRL) language. Our experiments show that RePReL framework not only achieves better performance and efficient learning on the task at hand but also demonstrates better generalization to unseen tasks. The interface layer allows for the RL and planner components to be a plug and play system and I demonstrate the versatility of our approach on several tasks. This is joint work with our PhD student Harsha Kokel, Prasad Tadepalli and Balaraman Ravindran.
* *Bio*: Prof. Sriraam Natarajan is a Professor at the Department of Computer Science at University of Texas Dallas and a RBDSCAI Distinguished Faculty Fellow at IIT Madras. His research interests lie in the field of Artificial Intelligence, with emphasis on Machine Learning, Statistical Relational Learning and AI, Reinforcement Learning, Graphical Models and Biomedical Applications. He is a AAAI senior member and has received the Young Investigator award from US Army Research Office, Amazon Faculty Research Award, Intel Faculty Award, XEROX Faculty Award, Verisk Faculty Award and the IU trustees Teaching Award from Indiana University. He is the AI and society track chair of AAAI 2022 and 2023, demo chair of IJCAI 2022, program co-chair of SDM 2020 and ACM CoDS-COMAD 2020 conferences. He was the speciality chief editor of Frontiers in ML and AI journal, and is an associate editor of MLJ, JAIR, DAMI and Big Data journals.


# Accepted submissions

- [*PG3: Policy-Guided Planning for Generalized Policy Generation*](papers/PRL2022_paper_1.pdf). Ryan Yang, Tom Silver, Aidan Curtis, Tomas Lozano-Perez and Leslie Kaelbling.
- [*Action Space Reduction for Planning Domains*](papers/PRL2022_paper_6.pdf). Harsha Kokel, Junkyu Lee, Michael Katz, Shirin Sohrabi and Kavitha Srinivas.
- [*Heuristic Search Planning with Deep Neural Networks using Imitation, Attention and Curriculum Learning*](papers/PRL2022_paper_17.pdf). Leah Chrestien, Tomáš Pevný, Stefan Edelkamp and Antonín Komenda.
- [*State Representation Learning for Goal-Conditioned Reinforcement Learning*](papers/PRL2022_paper_14.pdf). Lorenzo Steccanella and Anders Jonsson.
- [*Scaling up ML-based Black-box Planning with Partial STRIPS Models*](papers/PRL2022_paper_21.pdf). Matias Greco, Álvaro Torralba, Jorge A. Baier and Hector Palacios.
- [*Graph-Based Representation of Automata Cascades with an Application to Regular Decision Processes*](papers/PRL2022_paper_22.pdf). Alessandro Ronca and Giuseppe De Giacomo.
- [*Relational Abstractions for Generalized Reinforcement Learning on Symbolic Problems*](papers/PRL2022_paper_8.pdf). Rushang Karia and Siddharth Srivastava.
- [*Exploiting Multiple Levels of Abstractions in Episodic RL via Reward Shaping*](papers/PRL2022_paper_24.pdf). Roberto Cipollone, Giuseppe De Giacomo, Marco Favorito, Luca Iocchi and Fabio Patrizi.
- [*Compositional Reinforcement Learning from Logical Specifications*](papers/PRL2022_paper_27.pdf). Kishor Jothimurugan, Suguman Bansal, Osbert Bastani and Rajeev Alur.
- [*Deep Policy Learning for Perfect Rectangle Packing*](papers/PRL2022_paper_20.pdf). Boris Doux, Satya Tamby, Benjamin Negrevergne and Tristan Cazenave.
- [*Generalizing Behavior Trees and Motion-Generator (BTMG) Policy Representation for Robotic Tasks Over Scenario Parameters*](papers/PRL2022_paper_25.pdf). Faseeh Ahmad, Matthias Mayr, Elin Anna Topp, Jacek Malec and Volker Krueger.
- [*Speeding-up Continual Learning through Information Gaines in Novel Experiences*](papers/PRL2022_paper_26.pdf). Pierrick Lorang, Shivam Goel, Patrik Zips, Jivko Sinapov and Matthias Scheutz.
- [*An attention model for the formation of collectives in real-world domains*](papers/PRL2022_paper_16.pdf). Adrià Fenoy Barceló, Filippo Bistaffa and Alessandro Farinelli.

# Submission Procedure

We  solicit  workshop paper  submissions  relevant  to  the  above call  of  the
following types:

* Long papers -- up to 8 pages + unlimited references / appendices
* Short papers -- up to 4 pages + unlimited references / appendices
* Extended abstracts -- up to 2 pages + unlimited references / appendices

Please format submissions  in AAAI style (see instructions in [Author Kit 2021 at AAAI, http://www.aaai.org/Publications/Templates/AuthorKit22.zip](http://www.aaai.org/Publications/Templates/AuthorKit22.zip)). Authors considering
submitting to the workshop papers rejected from other conferences, please ensure
you  do  your  utmost to  address  the  comments given  by the reviewers.

**New**: NeurIPS format is also accepted with the same number of pages and references as the call-for-papers for the main-track.

Some accepted long  papers will be accepted as contributed  talks.  All accepted
long and short papers and extended abstracts  will be given a slot in the poster
presentation session.   Extended abstracts  are intended  as brief  summaries of
already published papers,  preliminary work, position papers  or challenges that
might help bridge the gap.

As the main purpose  of this workshop is to solicit  discussion, the authors are
invited to use the appendix of their submissions for that purpose.

[Paper submissions should be made through EasyChair](https://easychair.org/my/conference?conf=prl20220).

Please send your inquiries by email to the organizers at [prl.theworkshop@gmail.com](mailto:prl.theworkshop@gmail.com).

For up-to-date information, please visit the [PRL website, https://prl-theworkshop.github.io](https://prl-theworkshop.github.io).


## Previous Editions

- [PRL @ ICAPS 2021](https://prl-theworkshop.github.io/prl2021/)
- [PRL @ ICAPS 2020](https://prl-theworkshop.github.io/icaps20subpages.icaps-conference.org/workshops/prl/)

## Organizers

- [Michael Katz](https://resedit.watson.ibm.com/researcher/view.php?person=ibm-Michael.Katz1), IBM T.J. Watson Research Center, NY, USA
- [Hector Palacios](http://hectorpalacios.net/), ServiceNow Research, Montreal, Canada
- [Vicenç Gómez](https://www.upf.edu/web/vgomez), Universitat Pompeu Fabra, Barcelona, Spain

## Sponsor

<img src="servicenow-logo.jpg" width="20%" height="auto">
