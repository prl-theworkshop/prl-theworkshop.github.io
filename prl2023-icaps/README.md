# Bridging the Gap Between AI Planning and Reinforcement Learning ([PRL](https://prl-theworkshop.github.io) @ ICAPS 2023) – [Workshop at ICAPS 2023](https://icaps23.icaps-conference.org)

< [Link to other workshops in the series](https://prl-theworkshop.github.io)

ICAPS'23 Workshop \
Prague, Czech Republic  \
July 9, 2023

**Some of the accepted papers will be invited to be presented at the IJCAI edition of the workshop as well.**

## Aim and Scope of the Workshop

While AI Planning and Reinforcement Learning communities focus on similar
sequential decision-making problems, these communities remain somewhat unaware
of each other on specific problems, techniques, methodologies, and evaluations.

This workshop aims to encourage discussion and collaboration between researchers in the fields of AI planning and reinforcement learning. 
We aim to bridge the gap between the two communities, facilitate the discussion of differences and similarities in existing techniques, and encourage collaboration across the fields. 
We solicit interest from AI researchers that work in the
intersection of planning and reinforcement learning, in particular, those that focus on intelligent decision-making. This is the fifth edition of the [PRL workshop series](https://prl-theworkshop.github.io/) that started at [ICAPS 2020](https://icaps20subpages.icaps-conference.org/workshops/prl/).

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
* Reinforcement Learning and planning competition(s)
* Multi-agent planning and learning
* Applications of both reinforcement learning and planning 


## Important Dates

* Paper submission deadline (final): April 3rd, AOE
* Paper acceptance notification: April 27th, AOE 



ICAPS will be **in-person** this year. Authors of accepted workshop papers are expected to physically attend the conference and present in person.


## Schedule



| Time (Prague) | Title |
|:------------:|:-----------|
|     9:00     | Opening Remarks          |
|     9:10     |  **Session 1**            |
|  | [*Value Function Learning via Prolonged Backward Heuristic Search*](papers/value-function-learning.pdf). Zlatan Ajanovic, Bakir Lacevic, Jens Kober. |
|  | [*Learning General Policies with Policy Gradient Methods*](papers/learning-general-policies.pdf). Simon Ståhlberg, Blai Bonet, Hector Geffner. |
|  | [*Learning Hierarchical Policies by Iteratively Reducing the Width of Sketch Rules*](papers/learning-hierarchical-policies.pdf). Dominik Drexler, Jendrik Seipp, Hector Geffner. |
|  | [*Towards a Unified Framework for Sequential Decision Making*](papers/towards-a-unified-framework-for-sequential.pdf). Carlos Núñez-Molina, Pablo Mesejo, Juan Fernández-Olivares. |
|    10:30     | Coffee break |
|    11:00     | **Session 2**    |
|  | [*pyRDDLGym: From RDDL to Gym Environments*](papers/pyrddlgym-from-rddl-to-gym.pdf). Ayal Taitler, Michael Gimelfarb, Jihwan Jeong, Sriram Gopalakrishnan, Martin Mladenov, Xiaotian Liu, Scott Sanner. |
|  | [*Inapplicable Actions Learning for Knowledge Transfer in Reinforcement Learning*](papers/inapplicable-actions-learning.pdf). Leo Ardon, Alberto Pozanco, Daniel Borrajo, Sumitra Ganesh. |
|  | [*Multi-Agent Reinforcement Learning with Epistemic Priors*](papers/multi-agent-reinforcement-learning.pdf). Thayne T. Walker, Jaime S. Ide, Minkyu Choi, Michael John Guarino, Kevin Alcedo. |
|  | [*Mind the Uncertainty: Risk-Aware and Actively Exploring Model-Based Reinforcement Learning*](papers/mind-the-uncertainty.pdf). Marin Vlastelica, Sebastian Blaes, Cristina Pinneri, Georg Martius. |
|    12:20     | Lunch    |
|    13:40     | **Keynote**: [Sheila McIlraith - **Building Taskable RL Agents using Advice, Instructions, and AI Planning**](#sheila-mcilraith) |
|    14:40 | **Panel Discussion** [*Sequential decision making in the era of large language models*](#panel-discussion).  |
|    15:30     | Coffee break |
|    16:00     | **Closing remarks, discussion**         |
|    16:10     | **Poster Session**    |
|    18:00     | End      |


# Program

<!-- The event consists of: -->

<!-- * [Invited talk](#invited-speaker). 40 minutes for content + 10 minutes for questions.
	* [Sheila McIlraith](#sheila-mcilraith) 
* Talks for select accepted papers. 15 minutes for content + 5 minutes for questions.
* [Panel discussion](#panel). 60 minutes panel discussion.
* Poster session for all accepted papers. -->

<!-- # Invited Speaker -->
## [Sheila McIlraith](https://www.cs.toronto.edu/~sheila/) 
*Title*: **Building Taskable RL Agents using Advice, Instructions, and AI Planning**

<!-- 

* *Abstract*: Reinforcement Learning (RL) is proving to be a powerful technique for building sequential decision making systems in cases where the complexity of the underlying environment is difficult to model. Two challenges that face RL are reward specification and sample complexity. Specification of a reward function -- a mapping from state to numeric value -- can be challenging, particularly when reward-worthy behaviour is complex and temporally extended. Further, when reward is sparse, it can require millions of exploratory episodes for an RL agent to converge to a reasonable quality policy. In this talk I'll show how formal languages and automata can be used to represent complex non-Markovian reward functions. I'll present the notion of a Reward Machine, an automata-based structure that provides a normal form representation for reward functions, exposing function structure in a manner that greatly expedites learning. Finally, I'll also show how these machines can be generated via symbolic planning or learned from data, solving (deep) RL problems that otherwise could not be solved.
* *Bio*: Sheila McIlraith is a Professor in the Department of Computer Science, University of Toronto, a Faculty Member at the Vector Institute for Artificial Intelligence, and a Canada CIFAR AI Chair. McIlraith is the author of over 100 scholarly publications in the area of knowledge representation, automated reasoning and machine learning. Her work focuses on AI sequential decision-making broadly construed, through the lens of human-compatible AI.McIlraith is an AAAI Fellow, and an ACM Fellow. She is an associate editor of the Journal of Artificial Intelligence Research (JAIR), and a past associate editor of the journal Artificial Intelligence (AIJ). McIlraith served as program co-chair of AAAI-18, KR2012, and ISWC200. McIlraith's early work on Semantic Web Services has had a notable impact. In 2011 she and her co-authors were honoured with the SWSA 10-year Award, recognizing the highest impact paper from the International Semantic Web Conference, 10 years prior. Her research has also made practical contributions to the development of next-generation NASA space systems and to emerging Web standards. -->

## [Panel discussion](#panel-discussion)
* Topic: Sequential decision-making in the era of large language models
* Moderator: Christian Muise
* Panelists: Leslie P. Kaelbling, Subbarao Kambhampati, Erez Karpas, Michael Katz, ChatGPT (operated by Timo Gros).

## Talks 
Select accepted papers are given a slot in the program: 15 minutes for content + 5 minutes for questions.

## Poster session 
All accepted papers are expected to participate in the poster session


## List of Accepted Papers

* [oral+poster] [pyRDDLGym: From RDDL to Gym Environments](papers/pyrddlgym-from-rddl-to-gym.pdf) (Ayal Taitler, Michael Gimelfarb, Jihwan Jeong, Sriram Gopalakrishnan, Martin Mladenov, Xiaotian Liu, Scott Sanner)
* [oral+poster] [Inapplicable Actions Learning for Knowledge Transfer in Reinforcement Learning](papers/inapplicable-actions-learning.pdf) (Leo Ardon, Alberto Pozanco, Daniel Borrajo, Sumitra Ganesh)
* [poster only] [Meta-operators for Enabling Parallel Planning Using Deep Reinforcement Learning](papers/meta-operators-parallel-planning.pdf) (Ángel Aso Mollar, Eva Onaindia)
* [poster only] [Model Learning to Solve Minecraft Tasks](papers/model-learning-minecraft-tasks.pdf) (Yarin Benyamin, Argaman Mordoch, Roni Stern, Shahaf S. Shperberg)
* [oral+poster] [Towards a Unified Framework for Sequential Decision Making](papers/towards-a-unified-framework-for-sequential.pdf) (Carlos Núñez-Molina, Pablo Mesejo, Juan Fernández-Olivares)
* [poster only] [Policy Refinement with Human Feedback for Safe Reinforcement Learning](papers/policy-refinement-human-feedback.pdf) (Ali Baheri)
* [oral+poster] [Learning Hierarchical Policies by Iteratively Reducing the Width of Sketch Rules](papers/learning-hierarchical-policies.pdf) (Dominik Drexler, Jendrik Seipp, Hector Geffner)
* [oral+poster] [Learning General Policies with Policy Gradient Methods](papers/learning-general-policies.pdf) (Simon Ståhlberg, Blai Bonet, Hector Geffner)
* [oral+poster] [Mind the Uncertainty: Risk-Aware and Actively Exploring Model-Based Reinforcement Learning](papers/mind-the-uncertainty.pdf) (Marin Vlastelica, Sebastian Blaes, Cristina Pinneri, Georg Martius)
* [poster only] [Joint Learning of Policy with Unknown Temporal Constraints for Safe Reinforcement Learning](papers/joint-learning-policy-temporal-constraints.pdf) (Ali Baheri)
* [oral+poster] [Multi-Agent Reinforcement Learning with Epistemic Priors](papers/multi-agent-reinforcement-learning.pdf) (Thayne T. Walker, Jaime S. Ide, Minkyu Choi, Michael John Guarino, Kevin Alcedo)
* [poster only] [Preemptive Restraining Bolts](papers/preemptive-restraining-bolts.pdf) (Giovanni Varricchione, Natasha Alechina, Mehdi Dastani, Giuseppe De Giacomo, Brian Logan, Giuseppe Perelli)
* [poster only] [Hierarchical Planning for Rope Manipulation using Knot Theory and a Learned Inverse Model](papers/hierarchical-planning-rope-manipulation.pdf) (Matan Sudry, Tom Jurgenson, Aviv Tamar, Erez Karpas)
* [oral+poster] [Value Function Learning via Prolonged Backward Heuristic Search](papers/value-function-learning.pdf) (Zlatan Ajanovic, Bakir Lacevic, Jens Kober)


## Submission Details


We solicit workshop paper submissions relevant to the above call of the following types:

 * Long papers -- up to 8 pages + unlimited references / appendices
 * Short papers -- up to 4 pages + unlimited references / appendices
 * Extended abstracts -- up to 2 pages + unlimited references/appendices 
 
Please format submissions in AAAI style (see instructions in the [Author Kit](https://www.aaai.org/Publications/Templates/AuthorKit23.zip)). Authors submitting papers rejected from other conferences, please ensure you do your utmost to address the comments given by the reviewers. Please do not submit papers that are already accepted for the main ICAPS conference to the workshop.


Some accepted long papers will be invited for contributed talks. All accepted papers (long as well as short) and extended abstracts will be given a slot in the poster
presentation session.  Extended abstracts are intended as brief summaries of already published papers,  preliminary work, position papers, or challenges that
might help bridge the gap.

As the main purpose of this workshop is to solicit discussion, the authors are
invited to use the appendix of their submissions for that purpose.


Paper submissions should be made through [OpenReview](https://openreview.net/group?id=PRL/2023/ICAPS).


<!-- ### Workshop Proceedings (optional)

TODO

### Policy on Previously Published Materials (optional) 

TODO -->

<!-- ## Workshop Committee

TODO -->

### Organizing Committee

* Cameron Allen, Brown University, RI, USA 
* Timo P. Gros, Saarland University, Germany
* Michael Katz, IBM T.J. Watson Research Center, NY, USA
* Harsha Kokel, University of Texas at Dallas, TX, USA
* Hector Palacios, ServiceNow Research, Montreal, Canada
* Sarath Sreedharan, Colorado State University, CO, USA



Please send your inquiries to prl.theworkshop@gmail.com


<!-- ### Program Committee

TODO -->

<!-- ## List of Accepted Papers

TBD -->

<!-- ## Workshop Schedule

TBD -->


