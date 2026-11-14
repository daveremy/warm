---
title: "WARM v0.12 against Domain-Driven Design, Team Topologies and Data Mesh"
date: 2026-11-11
author: sagan (subagent)
tags: [research, warm, agents, prior-work]
---

# WARM v0.12 against Domain-Driven Design, Team Topologies and Data Mesh

2026-11-11. Method as in `synthesis.md`: each named concept of a source is listed with a verbatim definition and assigned to one WARM part, a span of several parts, design-time guidance with no WARM counterpart, or a misfit. A doubtful fit is called strained or a misfit. WARM text read: v0.12, Step 1 (with "What belongs in the platform"), Step 4 (all subsections), Step 5, "What WARM adds, and its limits", plus the Step 3 service table and the glossary to name parts.

One reader, no second rater. The reader knew WARM. "Precedent" below means "the source states the same thing", not "WARM copied it".

Sources read in full:
- Evans, *Domain-Driven Design Reference: Definitions and Pattern Summaries*, 2015, CC BY 4.0. https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf (59 PDF pages; text extracted with pypdf). Page references give the printed page and, in brackets, the PDF page.
- Team Topologies: https://teamtopologies.com/key-concepts (undated page); Skelton and Pais, "What is a Thinnest Viable Platform (TVP)?" https://teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp (2019-11-07); "What are the core team types in Team Topologies?" https://teamtopologies.com/key-concepts-content/what-are-the-core-team-types-in-team-topologies (2019-11-07); Platform Manifesto https://teamtopologies.com/platform-manifesto; Team API template https://github.com/TeamTopologies/Team-API-template (README, CC BY-SA 4.0); Skelton and Pais, "Team Cognitive Load", IT Revolution, 2021-01-19, "adapted from the book" https://itrevolution.com/articles/cognitive-load/.
- Dehghani, "How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh", 2019-05-20, https://martinfowler.com/articles/data-monolith-to-mesh.html (below: DM-2019); Dehghani, "Data Mesh Principles and Logical Architecture", 2020-12-03, https://martinfowler.com/articles/data-mesh-principles.html (below: DM-2020). Both read in full from the HTML; figures are images and were read by caption only.

---

## 1. Domain-Driven Design (Evans, DDD Reference 2015)

### 1A. Concepts, definitions and assignments

Strategic patterns are listed in full. Tactical and supple-design patterns are listed only where they bear on WARM.

| Concept | Verbatim definition (DDD Reference) | Assignment |
|---|---|---|
| domain | "A sphere of knowledge, influence, or activity. The subject area to which the user applies a program is the domain of the software." (p. vi [6]) | **Misfit** with WARM Domain. Evans's domain is the subject area. WARM's Domain is a charter for an area of work (goals, roles, workflow, knowledge, tools, rules, acceptance criteria). Evans's sense matches WARM's phrase "the subject of the work" in the platform test, not WARM's Domain. |
| model | "A system of abstractions that describes selected aspects of a domain and can be used to solve problems related to that domain." (p. vi [6]) | **Guidance, no counterpart.** Nearest is WARM's "Domain knowledge" row; WARM has no notion of one model per boundary. |
| ubiquitous language | "A language structured around the domain model and used by all team members within a bounded context to connect all the activities of the team with the software." (p. vi [6]); pattern: "Use the model as the backbone of a language. Commit the team to exercising that language relentlessly in all communication within the team and in the code." (p. 4 [11]) | **Guidance.** Strained link to Domain knowledge (Memory, Retrieval, Registry skills). WARM states no rule about consistent terms inside a domain, except in its parenthetical on bounded context. |
| context | "The setting in which a word or statement appears that determines its meaning. Statements about a model can only be understood in a context." (p. vi [6]) | **Misfit (word clash).** In WARM "context" means the context window the Harness manages. |
| bounded context | "A description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable." (p. vi [6], repeated p. 28 [35]); pattern: "Explicitly define the context within which a model applies. Explicitly set boundaries in terms of team organization, usage within specific parts of the application, and physical manifestations such as code bases and database schemas." (p. 2 [9]) | **Strained fit: Domain.** WARM already cites it (Step 4). Differences: a bounded context bounds a model and its terms; a WARM domain bounds a set of accountable responsibilities with a charter. Evans ties the boundary to "a subsystem, or the work of a particular team"; WARM keeps the domain separate from whoever fills its roles. |
| Continuous Integration | Pattern summary, p. 5 [12] (not quoted here: about keeping one model consistent inside a context) | **Guidance.** Out of WARM scope. |
| Layered Architecture | "Isolate the expression of the domain model and the business logic, and eliminate any dependency on infrastructure, user interface, or even application logic that is not business logic. Partition a complex program into layers." (p. 10 [17]) | **Span: Step 1 layers + platform test**, inside one program. Precedent for keeping domain logic apart from infrastructure; see 1B. |
| Entities | "When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in the model." (p. 11 [18]) | **Guidance.** Only an analogy to WARM's Agent vs Instance ("the agent is the identity, not the instance"). Not a counterpart. |
| Domain Events | "Model information about activity in the domain as a series of discrete events. Represent each event as a domain object. These are distinct from system events that reflect activity within the software itself" (p. 13 [20]) | **Span, strained: Messaging (events to subscribers) and Observability.** DDD's domain event is domain content; WARM's services carry events without meaning. |
| Services (DDD) | "When a significant process or transformation in the domain is not a natural responsibility of an entity or value object, add an operation to the model as a standalone interface declared as a service." (p. 14 [21]) | **Misfit (word clash).** A DDD service is a domain operation. A WARM service is a platform responsibility that "works the same whatever the work is about". |
| Modules | "Choose modules that tell the story of the system and contain a cohesive set of concepts." (p. 15 [22]) | **Guidance.** Parallel to WARM's "cohesive set of responsibilities" wording, at code scale. |
| Aggregates | "Cluster the entities and value objects into aggregates and define boundaries around each. Choose one entity to be the root of each aggregate ... give enforcement responsibility to the root" (p. 16 [23]) | **Guidance.** Bears on WARM's "exactly one domain is accountable": one owner enforces invariants for a boundary. Dinacode (section E) applies it to agents. No WARM part. |
| Repositories | "For each type of aggregate that needs global access, create a service that can provide the illusion of an in-memory collection of all objects of that aggregate's root type." (p. 17 [24]) | **Misfit.** Domain-specific access; not WARM Memory or Retrieval, which are domain-neutral. |
| Factories, supple design (pp. 18-27) | Object-level design patterns | **Not mapped**: single-program design, outside WARM's scope. |
| Context Map | "Identify each model in play on the project and define its bounded context. ... Name each bounded context, and make the names part of the ubiquitous language. Describe the points of contact between the models, outlining explicit translation for any communication, highlighting any sharing, isolation mechanisms, and levels of influence." (p. 29 [36]) | **Strained fit: Directory**, spanning "How domains depend on one another". Both are a record of the parts and how they relate. The context map records models, translations and influence; it does not record which part is accountable for which responsibility, or how to reach it. |
| upstream-downstream | "A relationship between two groups in which the 'upstream' group's actions affect project success of the 'downstream' group, but the actions of the downstream do not significantly affect projects upstream." (p. 28 [35]) | **Guidance.** WARM has no direction-of-influence concept between domains. |
| mutually dependent | "A situation in which two software development projects in separate contexts must both be delivered in order for either to be considered a success." (p. 28 [35]) | **Guidance.** |
| free | "A software development context in which the direction, success or failure of development work in other contexts has little effect on delivery." (p. 28 [35]) | **Guidance.** |
| Partnership | "Where development failure in either of two contexts would result in delivery failure for both, forge a partnership between the teams in charge of the two contexts. Institute a process for coordinated planning of development and joint management of integration." (p. 30 [37]) | **Guidance, no counterpart.** WARM has no joint-planning relation between domains. |
| Shared Kernel | "Designate with an explicit boundary some subset of the domain model that the teams agree to share. Keep this kernel small. ... This explicitly shared stuff has special status, and shouldn't be changed without consultation with the other team." (p. 31 [38]) | **Guidance; tension.** WARM calls two domains accountable for one scoped responsibility an "overlap" (a fault). DDD sanctions a small, explicitly shared part. |
| Customer/Supplier Development | "Establish a clear customer/supplier relationship between the two teams, meaning downstream priorities factor into upstream planning. Negotiate and budget tasks for downstream requirements ... Jointly developed automated acceptance tests can validate the expected interface from the upstream." (p. 32 [39]; the extracted text reads "t he", corrected here) | **Span, strained:** a handoff tracked by Orchestration plus WARM's "agreed in advance" (expected result) and Evaluation (acceptance tests). WARM has no priority-setting relation between domains. |
| Conformist | "Eliminate the complexity of translation between bounded contexts by slavishly adhering to the model of the upstream team." (p. 33 [40]) | **Guidance, no counterpart.** |
| Anticorruption Layer | "As a downstream client, create an isolating layer to provide your system with functionality of the upstream system in terms of your own domain model. This layer talks to the other system through its existing interface ... the layer translates in one or both directions as necessary between the two models." (p. 34 [41]) | **Strained fit: domain logic carried by Tools.** WARM: "A calculation, a connector to one bank ... are domain logic"; "The domain supplies that logic, and Tools carries it." WARM does not name translation as a concern. |
| Open-host Service | "Define a protocol that gives access to your subsystem as a set of services. Open the protocol so that all who need to integrate with you can use it." (p. 35 [42]) | **Misfit.** WARM gives defined interfaces to platform services and ordinary language to domain-to-domain requests. An OHS is a domain offering a defined protocol to other domains; WARM allows this only as "a brief with fixed fields, a required result format", a choice of the workflow. |
| Published Language | "Use a well-documented shared language that can express the necessary domain information as a common medium of communication, translating as necessary into and out of that language." (p. 36 [43]) | **Guidance.** Partial to WARM's "how much structure an exchange has ... is a choice of the workflow". |
| Separate Ways | "Declare a bounded context to have no connection to the others at all, allowing developers to find simple, specialized solutions within this small scope." (p. 37 [44]) | **Guidance.** |
| Big Ball of Mud | "Draw a boundary around the entire mess and designate it a big ball of mud. Do not try to apply sophisticated modeling within this context." (p. 38 [45]) | **Guidance.** Parallel to WARM Step 5: "A part that fits nowhere is a question ... the part may mix two responsibilities". |
| Core Domain | "Define a core domain and provide a means of easily distinguishing it from the mass of supporting model and code. ... Apply top talent to the core domain" (p. 40 [47]) | **Guidance, no counterpart.** WARM does not rank domains by value. |
| Generic Subdomains | "Identify cohesive subdomains that are not the motivation for your project. Factor out generic models of these subdomains and place them in separate modules. Leave no trace of your specialties in them. ... Also consider off-the-shelf solutions or published models for these generic subdomains." (p. 41 [48]) | **Strained fit: Platform (and Providers for off-the-shelf).** A close precedent for the platform test; see 1B. Difference: a generic subdomain is still domain model (e.g. a calendar), not a service for agents. |
| supporting subdomain | **Not found in the source read.** The Reference uses "supporting" only as an adjective ("the mass of supporting model and code", p. 40; "supporting players", p. 45). The three-way core/supporting/generic classification is in Vernon, *Implementing Domain-Driven Design* (2013), not read. Dubrov (covered in `2026-11-11-warm-prior-work-reading.md`) uses it. | — |
| Domain Vision Statement | "Write a short description (about one page) of the core domain and the value it will bring, the 'value proposition.'" (p. 42 [49]) | **Strained fit: Domain Goals.** |
| Highlighted Core, Segregated Core, Abstract Core (pp. 43, 45, 46) | Ways to make the core visible in the code | **Guidance.** |
| Cohesive Mechanisms | "Partition a conceptually cohesive mechanism into a separate lightweight framework. ... Now the other elements of the domain can focus on expressing the problem ('what'), delegating the intricacies of the solution ('how') to the framework." (p. 44 [51]) | **Strained fit: platform test** ("the platform supplies mechanisms and a domain supplies meaning"). Inside one program. |
| Large-scale Structure | "Devise a pattern of rules or roles and relationships that will span the entire system and that allows some understanding of each part's place in the whole—even without detailed knowledge of the part's responsibility." (p. 47 [54]) | **Span.** WARM as a whole is a structure of this kind. |
| Evolving Order | "Let this conceptual large-scale structure evolve with the application ... it is best not to shoot for comprehensiveness, but rather to find a minimal set that solves the problems that have emerged." (p. 48 [55]) | **Guidance.** |
| System Metaphor | "When a concrete analogy to the system emerges that captures the imagination of team members ... adopt it as a large-scale structure." (p. 49 [56]) | **Guidance.** WARM uses analogies (a department's charter, a company directory) without making them a structure. |
| Responsibility Layers | "If you identify natural strata in the domain, cast them as broad abstract responsibilities. ... Refactor the model so that the responsibilities of each domain object, aggregate, and module fit neatly within the responsibility of one layer." (p. 50 [57]) | **Strained fit: Step 1 layers and Step 3 ("each service has one responsibility").** |
| Knowledge Level | "Create a distinct set of objects that can be used to describe and constrain the structure and behavior of the basic model. Keep these concerns separate as two 'levels,' one very concrete, the other reflecting rules and knowledge that a user or super-user is able to customize." (p. 51 [58]) | **Strained fit: domain rules supplied to Policy** ("the Communications domain supplies it, and the platform applies it"). |
| Pluggable Component Framework | "Distill an abstract core of interfaces and interactions and create a framework that allows diverse implementations of those interfaces to be freely substituted." (p. 52 [59]) | **Strained fit: Step 5** ("A builder who keeps each service behind a clear interface can change its supplier with less rework"). |

### 1B. What WARM states that DDD already states

- **An area of work kept separate from who does the work.** Partial. Evans defines the bounded context as a description of a boundary, and lists team organization as one of the ways to set it: "Explicitly set boundaries in terms of team organization, usage within specific parts of the application, and physical manifestations such as code bases and database schemas" (p. 2). The definition itself attaches it to "a subsystem, or the work of a particular team" (p. vi). DDD does not discuss filling roles with agents or people.
- **A shared platform serving several areas.** Partial, at code scale: Generic Subdomains ("Factor out generic models of these subdomains and place them in separate modules", p. 41) and Cohesive Mechanisms (p. 44). DDD does not describe a platform shared by several bounded contexts.
- **A test for what belongs in the platform.** Close precedents, stated inside one design: "Leave no trace of your specialties in them" (Generic Subdomains, p. 41); "the other elements of the domain can focus on expressing the problem ('what'), delegating the intricacies of the solution ('how') to the framework" (Cohesive Mechanisms, p. 44); "Isolate the expression of the domain model and the business logic, and eliminate any dependency on infrastructure" (Layered Architecture, p. 10). None is phrased as a test of whether a responsibility "works the same whatever the work is about".
- **One accountable owner per responsibility.** Not stated at the level of contexts. At object level: "give enforcement responsibility to the root" (Aggregates, p. 16). Shared Kernel explicitly allows shared ownership of a small part (p. 31).
- **A record of who is responsible for what.** Partial: the Context Map ("Identify each model in play ... Name each bounded context ... Describe the points of contact", p. 29). It records models and relations, not accountability or how to reach a role.
- **How areas relate and hand work over.** Strong precedent, more detailed than WARM: the context-map relationships (partnership, shared kernel, customer/supplier, conformist, anticorruption layer, open host service, published language, separate ways) and the upstream/downstream, mutually dependent and free terms (pp. 28-38).
- **Governance shared across areas.** Not found. DDD names no cross-context governance body or mechanism, other than agreed shared kernels and published languages.

### 1C. What DDD has that WARM lacks

1. A typology of relationships between areas (nine named patterns), and the idea of direction of influence (upstream/downstream).
2. Translation as a named concern between areas (anticorruption layer, published language, open host service). WARM says domains talk in "ordinary language" and "sort out what was unclear", and names no translation step.
3. Prioritization among areas (core domain, domain vision statement, generic subdomains given "lower priority").
4. A sanctioned form of shared ownership (shared kernel), where WARM sees only "overlap".
5. A pattern for an area with no clear boundaries (big ball of mud) as a deliberate designation.
6. The rule that terms have one meaning inside a boundary and may differ across boundaries (ubiquitous language, context). WARM mentions it once in a parenthetical and does not use it.

### 1D. Same word, different meaning

| Word | DDD | WARM |
|---|---|---|
| domain | "A sphere of knowledge, influence, or activity. The subject area to which the user applies a program" | An area of work defined by a charter; "A domain does not act". |
| context | "The setting in which a word or statement appears that determines its meaning" | The model's context window (Harness). |
| service | A domain operation that is "not a natural responsibility of an entity or value object" | A platform responsibility; "Only the platform has services; a domain does work." |
| pattern | A named problem-solution pair in a pattern language (the Reference is "Definitions and Pattern Summaries") | WARM does not define "pattern". It offers a "template for workflow". |
| layer | Layers inside one program (UI, application, domain, infrastructure) | Five logical layers of a system (People, Domains, Platform, Infrastructure, Providers). DDD's "infrastructure" layer is code; WARM's is machines and network. |
| model | The domain model, a system of abstractions | WARM uses "model" for a language model and for WARM itself ("reference model"). |
| platform | Used once, informally: "a steady platform from which to explore models" (p. 19) | The layer of shared services. |
| product | Not a term in the Reference | "work product", "harness product". |

---

## 2. Team Topologies (Skelton and Pais, 2019)

The book itself was not read (not available without purchase). Definitions come from the authors' site, their GitHub template and their IT Revolution excerpt.

### 2A. Concepts, definitions and assignments

| Concept | Verbatim definition, source | Assignment |
|---|---|---|
| Team Topologies (the approach) | "Team Topologies is an approach to designing team-of-teams organizations for fast flow of value." (key-concepts) | Scope differs: an organization design for teams of people. |
| Stream-aligned team | "Stream-aligned team: aligned to a flow of work from (usually) a segment of the business domain" (key-concepts). Also: "Stream-aligned teams own an entire slice of the business domain (or other flow) end-to-end. The Stream-aligned teams are 'You Built It, You Run It' teams. There are no hand-offs to other teams for any purpose." (key-concepts) | **Span: Domain + the agents and people who fill its roles.** TT's unit is a team of people; WARM separates the area of work from who fills it. The "no hand-offs" sentence conflicts with WARM Step 4, which makes handoffs between domains normal. |
| Enabling team | "Enabling team: helps a Stream-aligned team to overcome obstacles. Also detects missing capabilities." (key-concepts); "Enabling teams temporarily boost skills in other teams, then move on." (key-concepts) | **Guidance, no counterpart.** Nearest WARM parts: Improvement (proposed changes) and skills in the Registry. WARM has no temporary helper role across domains. |
| Complicated Subsystem team | "Complicated Subsystem team: where significant mathematics/calculation/technical expertise is needed." (key-concepts) | **Strained fit: a domain that receives work "because of skill and tools"** (WARM's research example). Not a platform service in WARM's sense, because its work depends on the subject. |
| Platform team | "Platform team: a grouping of other team types that provide a compelling internal product to accelerate delivery by Stream-aligned teams" (key-concepts); "Platform teams create services that accelerate stream-aligned teams, removing complexity." (key-concepts) | **Strained fit: Platform layer**, with the difference that TT names the team, WARM names the services. WARM records "who supplies ... who operates" a service in a mapping (Step 5), not as a team. |
| Collaboration (mode) | "Collaboration: working together for a defined period of time to discover new things (APIs, practices, technologies, etc.)" (key-concepts) | **Strained fit: "How domains depend on one another"** ("the two sort out what was unclear"). TT bounds it in time; WARM does not. |
| X-as-a-Service (mode) | "X-as-a-Service: one team provides and one team consumes something 'as a Service'" (key-concepts); "Consuming or providing with minimal interaction (low cost, clear boundaries)" (key-concepts) | **Strained fit: how an agent reaches a platform service** ("through a defined interface, with stated guarantees"). TT also uses it between non-platform teams. |
| Facilitation (mode) | "Facilitation: one team helps and mentors another team" (key-concepts) | **Guidance, no counterpart.** |
| Cognitive load | "Cognitive load was characterized in 1988 by psychologist John Sweller as 'the total amount of mental effort being used in the working memory.'" with intrinsic, extraneous and germane kinds (IT Revolution, 2021). Key-concepts: "Teams can only handle so much complexity before breaking down. Each new tool, responsibility or domain your team is given taxes their mental bandwidth." | **Guidance, no counterpart.** WARM's nearest statement is guidance from experience: unattended work "filled the conversation's context" and was moved out (Step 4, "How work starts"). The authors' 2026 posts map team cognitive load to an agent's context window (section E), which is WARM's Harness. |
| Thinnest Viable Platform | "The TVP approach creates platforms that provide just enough capability without unnecessary complexity." (key-concepts); "This TVP could be just a wiki page if that's all you need for your platform ... If that's all you need don't build anything else, you're still running on a platform but you don't make it any thicker than necessary" (TVP page, 2019) | **Guidance.** Partial parallel: WARM says "a system does not need all twenty-five" and "A system with one agent needs no agent messaging; Messaging is still a platform service." TT sizes the platform by need; WARM places a responsibility regardless of current use. |
| Platform as a product | "The platforms we're talking about have placed a strong focus on developer experience, they see other development teams as their customers effectively. They run the platform as a product or service" (TVP page, 2019). Platform Manifesto: "unblocking internal customers via self-service patterns". The term "Platform-as-a-Product" appears on key-concepts only as a course topic. | **Guidance, no counterpart.** WARM gives a service "stated guarantees" but has no customer relation between platform and domains. |
| Team API | "A Team API is a description and specification that a team can define that tells others how to interact with that team." Fields include "Team name and focus", "Team type", "Do we provide a service to other teams?", "What kind of Service Level Expectations do other teams have of us?", "Software owned and evolved by this team", "Chat tool channels", and a table of "Teams we currently interact with" with "Interaction Mode", "Purpose", "Duration". (Team-API-template README) | **Strained fit: Directory entry plus Domain charter.** Shared: what the unit is responsible for ("focus", "software owned") and how to reach it ("chat tool channels"). Different: the Team API is written by each team about itself; WARM's Directory is one lookup whose content "people set". |
| Principle: Eliminate Team Dependencies | "Nothing kills productivity faster than one team waiting on another team. ... Fix the handoffs, not just the teams." (key-concepts) | **Guidance.** Bears on WARM handoffs; see 2D. |
| Pattern: Flexible Team Boundaries | "The best companies enable teams to negotiate boundary changes directly rather than wait for top-down directives." (key-concepts) | **Guidance; tension.** WARM: "People set this division, as part of directing the domains." |
| Pattern: Continuous Adaptation | "Organizational design is never 'done'—it must evolve ... Building feedback loops that identify when adjustments are needed" (key-concepts) | **Strained fit: Improvement** and the "improve" stage of WARM's workflow template. |
| Stewardship boundary (2026, new) | "the stewardship boundary around the value flow remains the remit of the human team" (teamtopologies.com/ai-workforce-readiness); "every AI agent and automated workflow is governed by a specific, long-lived team" (Skelton, 2026-08-18, see E) | **Strained fit: Domain Goals ("who is accountable") and Identity ("record the person accountable for each agent identity").** |

### 2B. What WARM states that Team Topologies already states

- **An area of work kept separate from who does the work.** Not found. TT defines the unit as a team aligned to a stream; area and team are one. The 2026 stewardship posts keep the boundary with "the human team".
- **A shared platform serving several areas.** Yes: "Platform team: a grouping of other team types that provide a compelling internal product to accelerate delivery by Stream-aligned teams" (key-concepts).
- **A test for what belongs in the platform.** Not as a test. The criterion is the effect on the user team: "A good platform should make stream-aligned teams move faster, not generate more dependencies to manage" (key-concepts). Fowler's summary (secondary, https://martinfowler.com/bliki/TeamTopologies.html) puts it as platforms that take "care of these non-focal concerns".
- **One accountable owner per responsibility.** Implied by "own": "Stream-aligned teams deliver direct value to customers along a value stream. They own the outcomes." (key-concepts). "Software owned and evolved by this team" in the Team API.
- **A record of who is responsible for what.** Partial: the Team API, one per team, with focus, owned software, services provided and contact channels. No central lookup is described.
- **How areas relate and hand work over.** Yes, a typology: three interaction modes, "There are only three ways in which team should interact" (key-concepts). But TT's stated aim is to remove handoffs ("There are no hand-offs to other teams for any purpose").
- **Governance shared across areas.** Not found in the pages read.

### 2C. What Team Topologies has that WARM lacks

1. A small fixed set of interaction modes, each with a cost ("high bandwidth, high cost"; "low cost, clear boundaries") and an expected duration, and the advice to change mode over time.
2. Cognitive load as a sizing rule for an area of work: "Explicitly thinking about cognitive load can be a powerful tool for deciding on team size, assigning responsibilities, and establishing boundaries with other teams" (IT Revolution). WARM has no rule for how large a domain may be.
3. Temporary helper roles (enabling team, facilitation).
4. Platform as a product: internal customers, developer experience, sizing to need (TVP).
5. A self-description per unit (Team API) with service-level expectations and current interactions.
6. Explicit design for change of boundaries over time (flexible boundaries, continuous adaptation).

### 2D. Same word, different meaning

| Word | Team Topologies | WARM |
|---|---|---|
| domain | "a segment of the business domain"; also "Each new tool, responsibility or domain your team is given" (a subject area a team covers) | An area of work with a charter. |
| platform | A team grouping that provides "a compelling internal product"; can be "just a wiki page" | A layer of services for agents. |
| product | The platform is run "as a product or service"; teams see others "as their customers" | "work product" and "harness product"; WARM has no product relation between platform and domains. |
| pattern | "The Six Patterns ... tell you how" (key-concepts) | Not defined. |
| service | Anything provided "as a Service" by one team to another | A platform responsibility only. |
| team | A stable group of people, the unit of design | WARM uses "team" for "a coordinating agent and task agents" (Step 4). |
| hand-off | Something to eliminate ("no hand-offs to other teams for any purpose") | A normal, tracked event ("it hands the work over and gets a result back"). |
| API | "Team API": a team's description for other teams | WARM uses "defined interface" for platform services only. |

---

## 3. Data Mesh (Dehghani, 2019 and 2020)

### 3A. Concepts, definitions and assignments

| Concept | Verbatim definition, source | Assignment |
|---|---|---|
| Data mesh (four principles) | "four underpinning principles that any data mesh implementation embodies ... 1) domain-oriented decentralized data ownership and architecture, 2) data as a product, 3) self-serve data infrastructure as a platform, and 4) federated computational governance." (DM-2020) | Scope differs: analytical data in an enterprise. |
| Domain | Example: "'podcasts', teams and systems that manage podcast publication and their hosts" (DM-2020); "Our organizations today are decomposed based on their business domains." (DM-2020) | **Span: Domain + the people and systems in it.** DM's domain is an organizational unit with its teams and systems. WARM separates the definition from who fills it. |
| Domain ownership | "Data mesh, at core, is founded in decentralization and distribution of responsibility to people who are closest to the data in order to support continuous change and scalability." ... "Data mesh follows the seams of organizational units as the axis of decomposition." (DM-2020) | **Strained fit: Domain responsibilities and "exactly one domain is accountable".** |
| Source-aligned and consumer-aligned domain data | "Some domains naturally align with the source, where the data originates." / "Some domains align closely with the consumption." (DM-2019) | **Guidance, no counterpart.** |
| Distributed pipelines as domain internal implementation | "a data pipeline is simply an internal complexity and implementation of the data domain and is handled internally within the domain." (DM-2019) | **Strained fit:** WARM's "Domain work may be a fixed script ... domain logic". |
| Data as a product | "Analytical data provided by the domains must be treated as a product, and the consumers of that data should be treated as customers" (DM-2020) | **Misfit.** WARM has work products (stored by Artifacts) but no notion of a domain's standing offering to other domains with customers. |
| Data product (architectural quantum) | "Data product is the node on the mesh that encapsulates three structural components required for its function, providing access to the domain's analytical data as a product": "Code", "Data and Metadata", "Infrastructure". (DM-2020) | **Misfit / span** (domain logic + Artifacts + Environments). |
| Discoverable | "A common implementation is to have a registry, a data catalogue, of all available data products with their meta information such as their owners, source of origin, lineage, sample datasets, etc. ... Each domain data product must register itself with this centralized data catalogue for easy discoverability." (DM-2019) | **Span: Registry + Directory.** A central catalogue that records owners. It records owners of data products, not which domain is accountable for a responsibility, and entries are self-registered, not set by people. |
| Addressable | "A data product, once discovered, should have a unique address following a global convention that helps its users to programmatically access it." (DM-2019) | **Strained fit: Directory ("how to reach a role").** |
| Trustworthy and truthful | "Each data product defines and assures the target level of its integrity and truthfulness as a set of SLOs." (DM-2019) | **Span: Domain acceptance criteria + Evaluation.** |
| Self-describing semantics and syntax | "Quality products require no consumer hand holding to be used: they can be independently discovered, understood and consumed." (DM-2019) | **Guidance.** |
| Inter-operable and governed by global standards | "Such standardizations should belong to a global governance, to enable interoperability between polyglot domain datasets." (DM-2019) | **Span: Governance (Policy) + People.** |
| Secure and governed by a global access control | "the access control policies can be defined centrally but applied at the time of access to each individual dataset product." (DM-2019) | **Clean fit: Identity + Policy** (rule supplied centrally, enforced at point of use). |
| Data product owner | "A data product owner makes decisions around the vision and the roadmap for the data products, concerns herself with the satisfaction of her consumers ... She is responsible for the lifecycle of the domain datasets" (DM-2019) | **Strained fit: a Role in a domain, accountable for Goals.** |
| Data product developer / data engineers | "Each domain will include data product developer roles, responsible for building, maintaining and serving the domain's data products." (DM-2020) | **Clean fit: Roles.** |
| Self-serve data infrastructure as a platform | "The key to building the data infrastructure as a platform is (a) to not include any domain specific concepts or business logic, keeping it domain agnostic, and (b) make sure the platform hides all the underlying complexity and provides the data infrastructure components in a self-service manner." (DM-2019) | **Clean fit: Platform layer, with a placement test.** See 3B. |
| Platform plane | "A plane is representative of a level of existence - integrated yet separate. ... A plane is neither a layer and nor implies a strong hierarchical access model." (DM-2020) | **Misfit** as a structure; WARM uses layers and groups. |
| Data infrastructure provisioning plane | "supports the provisioning of the underlying infrastructure, required to run the components of a data product and the mesh of products." (DM-2020) | **Span: Infrastructure + Environments.** |
| Data product developer experience plane | "It uses simple declarative interfaces to manage the lifecycle of a data product. It automatically implements the cross-cutting concerns that are defined as a set of standards and global conventions, applied to all data products and their interfaces." (DM-2020) | **Span: Platform (Releases, Registry, Policy).** |
| Data mesh supervision plane | "there are a set of capabilities that are best provided at the mesh level - a graph of connected data products - globally. ... ability to discover data products for a particular use case, is best provided by search or browsing the mesh" (DM-2020) | **Span: Directory/Registry discovery + Retrieval across domains.** |
| Federated computational governance | "A decision making model led by the federation of domain data product owners and data platform product owners, with autonomy and domain-local decision making power, while creating and adhering to a set of global rules - rules applied to all data products and their interfaces" (DM-2020) | **Span: Governance group (Policy) + People.** WARM says "Domains and the platform's operator supply the rules" and Policy enforces them, but names no federation that sets global rules. |
| Computational policies embedded in the mesh | "they need to comply with the modeling of quality and specification of SLOs based on a global standard, defined by the global federated governance team, and automated by the platform." (DM-2020) | **Clean fit: rules supplied, Policy applies** (WARM: "the Communications domain supplies it, and the platform applies it"). |
| Polysemes | "Responsible for modeling polysemes - data elements that cross the boundaries of multiple domains" (DM-2020 table) | **Guidance, no counterpart.** |
| Operational vs analytical planes | "Today's landscape is divided into operational data and analytical data." (DM-2020) | **Misfit**, out of scope. |

### 3B. What WARM states that Data Mesh already states

- **An area of work kept separate from who does the work.** Not found. A domain is "teams and systems that manage" something.
- **A shared platform serving several areas.** Yes: "Harvesting and extracting domain agnostic infrastructure capabilities into a data infrastructure platform solves the need for duplicating the effort of setting up data pipeline engines, storage, and streaming infrastructure." (DM-2019)
- **A test for what belongs in the platform.** Yes, stated as a design rule: "(a) to not include any domain specific concepts or business logic, keeping it domain agnostic" (DM-2019). This is the same criterion as WARM's "A responsibility belongs to the platform if it works the same whatever the work is about". It is also the same move as WARM's "A reusable responsibility discovered inside a domain is treated as a gap in the platform": DM-2019 extracts duplicated per-domain capability into the platform.
- **One accountable owner per responsibility.** Yes for data: "The accountability of data quality shifts upstream as close to the source of the data as possible." (DM-2020); the data product owner "is responsible for the lifecycle of the domain datasets" (DM-2019).
- **A record of who is responsible for what.** Partial: "a registry, a data catalogue, of all available data products with their meta information such as their owners" (DM-2019). It lists products and owners, not responsibilities, and each product registers itself.
- **How areas relate and hand work over.** Partial: "each domain can have dependencies to other domains' operational and analytical data endpoints" (DM-2020); a "serving and pull model across all domains" (DM-2019). Only data is exchanged; no request-and-result handoff.
- **Governance shared across areas.** Yes, the fourth principle (federated computational governance), with the split "what shall be standardized globally, implemented and enforced by the platform for all domains ... and what shall be left to the domains to decide" (DM-2020).
- **The model shape itself.** DM puts domains, a shared self-serve platform and cross-domain governance in one model. WARM's layer structure (Domains on Platform, Governance across) has the same shape for agent work.

### 3C. What Data Mesh has that WARM lacks

1. A domain's standing offering to other domains, treated as a product with consumers, qualities (discoverable, addressable, trustworthy, self-describing, interoperable, secure) and SLOs.
2. A governance body made of domain representatives that sets global rules, with an explicit list of what is global and what is local, and the instruction that the platform automates the global rules.
3. Treatment of entities that cross domain boundaries (polysemes, federated identifiers).
4. Success measures for the platform ("lowering the 'lead time to create a new data product'", DM-2019) and for governance ("the network effect").
5. Planes: groups of platform capabilities by the kind of user they serve, explicitly not a hierarchy.

### 3D. Same word, different meaning

| Word | Data Mesh | WARM |
|---|---|---|
| domain | A business domain as an organizational unit, with its teams and systems; DM uses "the business domain's bounded context" as the boundary | An area of work defined by a charter, separate from who fills it. |
| platform | "Self-serve data infrastructure as a platform"; DM-2019 also calls the whole mesh "a ubiquitous data mesh as a platform" | The layer of shared services. |
| product | "data product": code, data, metadata and infrastructure, owned by a domain, with consumers | "work product" (output of a task), "harness product". |
| plane | "A plane is neither a layer and nor implies a strong hierarchical access model" | WARM has layers and groups, no planes. |
| governance | A federated decision-making model plus computational enforcement | A group of four services (Identity, Secrets, Policy, Approvals). |
| registry / catalog | A catalog ("data catalogue" in the source) of data products and their owners | Registry holds versioned definitions of agents, tools and skills; Directory records accountability. |
| context | "bounded context" (from DDD); "multiple interpretive contexts" | Context window. |

---

## E. Published applications to systems of AI agents

Excluded as already covered in `research/reports/2026-11-11-warm-prior-work-reading.md`: Miles (Engineering Agents), Dubrov, Atlan bounded-context spaces.

**How I searched (2026-11-11).**
- arXiv API (export.arxiv.org, abstract field, sorted by date): `abs:"team topologies"` (3 hits, none applies TT); `abs:"data mesh" AND (agent OR agents OR agentic)` (1); `abs:"domain-driven design" AND (agent OR agents OR agentic)` (0); `abs:"domain driven design" AND (...)` (0); `abs:"bounded contexts" AND (agent OR agents)` (33, all reviewed by title; none applies DDD; they use the phrase for a limited context window); `abs:"data product" AND abs:agentic` (21, two relevant); `abs:"context map" AND abs:agent` (4, none applies DDD).
- Web search: "Zhamak Dehghani AI agents data mesh agentic 2025"; "Team Topologies AI agents stream-aligned agent team platform team agentic"; "domain-driven design multi-agent LLM bounded context agents"; "agentic mesh OR agentic AI mesh"; "Broda Agentic Mesh"; "arxiv LLM multi-agent Conway's law OR team topologies OR context mapping".
- Pages were fetched raw and quotes taken from the HTML text, except where marked.

### Team Topologies applied to agents

1. **Skelton, "Team Topologies for the AI age - stewardship of value flow", teamtopologies.com, 2026-08-18.** https://teamtopologies.com/news-blogs-newsletters/team-topologies-for-the-ai-age-stewardship-of-value-flow. The authors' own move from team ownership to "stewardship boundaries" that cover agents. Quote: "Clear stewardship boundaries solve this problem by ensuring that every AI agent and automated workflow is governed by a specific, long-lived team." Also: "Engineering leaders ... have mapped team cognitive load directly to AI context windows."
2. **Team Topologies, "How do Team Topologies principles support an organization's readiness for agentic AI?", 2026-08-12** (no byline). https://teamtopologies.com/news-blogs-newsletters/how-do-team-topologies-principles-support-an-organizations-readiness-for-agentic-ai. Quote: "In the context of agentic AI, this human cognitive boundary directly maps to an AI agent's context window."
3. **Team Topologies, AI Workforce Readiness page** (undated). https://teamtopologies.com/ai-workforce-readiness. Commercial page. Quote: "Team Topologies provides the organizational architecture for teams and services ... to enable teams of humans, hybrid teams of humans + AI assistance, and full Agentic AI to act with 'bounded agency' to achieve goals and outcomes."
4. **InfoQ, report of Skelton's QCon London 2026 talk, Mark Silvester, 2026-03-31.** https://www.infoq.com/news/2026/03/ai-agency-team-topologies. Secondary report of a talk. Quote: "Skelton argued that the principles found in the original Team Topologies framework provide the necessary infrastructure for agency. This starts with trust founded on bounded agency, a concept where the authority to act is intentionally constrained by rules and guardrails".
5. **Olivier Wulveryck, "Who Does What? Team Topologies for the Agentic Platform", 2026-06-22 (last modified 2026-10-08).** https://blog.owulveryck.info/2026/06/22/who-does-what-team-topologies-for-the-agentic-platform.html. Applies the four team types to building and using an "agentic platform"; the author notes it was AI-translated and criticized on Hacker News. Quote: "This is exactly what the agentic platform does: it absorbs technical complexity so that business teams carry only the cognitive load of their domain."
6. **wal.sh, "Who Does What, With Agents: A CTO's Read of Team Topologies for the Agentic Platform"** (undated; annotation dated 2026-10-08). https://wal.sh/research/team-topologies-agentic/. A re-reading of Wulveryck for one or two people plus agents. Quote: "Four teams become four hats. Three interaction modes become a schedule."
7. **Rework, "Team Topologies for Human-Plus-Agent Teams: Where Agents Actually Fit", 2026-09-22.** https://resources.rework.com/libraries/ai-future-of-work/team-topologies-for-human-plus-agent-teams. Vendor resource page. Quote: "The honest answer is that agents don't create a fifth team type."
8. **Gravitee "corpus" pages** (https://gravitee.io/corpus/gen-966/organizational-theory/team-topologies.html and a platform-engineering companion). Vendor pages; the fetch returned only site navigation, so no quote. Found by search only; contents not verified.

### Domain-Driven Design applied to agents (new beyond the earlier reading)

9. **Dinacode, "DDD for multi-agent systems", 2026-05-06.** https://www.dinacode.com/en/blog/ddd-multi-agent-systems. Consultancy blog. Maps agent = bounded context and uses aggregates for write ownership. Quotes: "Applied to multi-agent systems, it offers the precise framework: each agent as a bounded context, aggregates as state owners, explicit translation when two agents communicate." and "When an agent needs a change outside its aggregate, it doesn't write directly — it issues a request to the owning agent, which validates with its rules."
10. **Andrey Chauzov, "Domain-driven design for AI systems: architectural patterns and production experience", 2025 (page dates 2025-10-29 and 2025-11-04).** https://avchauzov.github.io/blog/2025/domain-driven-design-ai-systems. Personal blog; reports figures from "internal benchmarks" without method. Quote: "The problem of 'agent sprawl' is solved by aligning each agent with a specific Bounded Context."
11. **GitNation talk, "From Prompt Spaghetti to Bounded Contexts: DDD for Agentic Codebases".** https://gitnation.com/contents/from-prompt-spaghetti-to-bounded-contexts-ddd-for-agentic-codebases. Fetch returned no text. Title only; not read.
12. Further titles found by search and **not read**: "Domain Driven Design in the AI Era: From Models to Meaning" (nidly.substack.com); "Why DDD Will Come Back for AI Agents?" (sohit.substack.com); "LLM Agents, Part 3 - Multi-Agent LLM Products: A Design Pattern Perspective" (aisc.substack.com).

### Data Mesh applied to agents

13. **Dehghani, "Autonomous Data Products for the Autonomous Era: Rethinking Data Architecture for GenAI", QCon AI New York 2025 (abstract).** https://newyork.qcon.ai/presentation/newyork2025/autonomous-data-products-autonomous-era-rethinking-data-architecture-genai. Agents as consumers of data products. Quote (conference abstract, not her text): "Existing platforms, optimized for human interpretation and batch-oriented analytics, are misaligned with the operational realities of autonomous agents that consume, reason over, and act upon data continuously at machine scale."
14. **Nextdata (Dehghani's company), "2025: The Year Data Became the Bottleneck for AI", by Cornelius Willis.** https://www.nextdata.com/our-pov/2025-the-year-data-became-the-bottleneck-for-ai. Vendor post. Quote: "Data 3.0: autonomous data products that collapse pipelines, embed governance by default, and deliver AI-ready data directly to applications and agents."
15. **Eric Broda and Davis Broda, *Agentic Mesh*, O'Reilly, 2026.** O'Reilly pages returned 403 (blocked). Known only from search-result summaries, which say it builds "on API service mesh and data mesh concepts" and covers "agent registries, marketplaces, trust-building mechanisms, and human-in-the-loop oversight". Secondary; not verified. Eric Broda is described as co-author of *Implementing Data Mesh*. This is the most likely published work to apply data-mesh ideas to the organization of agents themselves; it should be read.
16. **DXC, "Data Mesh, AI Mesh, enterprise data connectivity", 2025-11-11.** https://dxc.com/insights/knowledge-base/data-mesh-ai-mesh-enterprise-data-connectivity. Vendor page. Quote: "AI Mesh extends Data Mesh principles to AI systems, creating a distributed network of AI agents that dynamically access underlying sources."
17. **Confluent Current New Orleans 2025, "Agents Running A Data Mesh".** https://current.confluent.io/post-conference-videos-25/agents-running-a-data-mesh-e-nola25. Talk abstract. Quote: "This presentation introduces a novel Agentic Data Mesh architecture where AI agents take on proactive roles in the data product development lifecycle."
18. **Tonnarelli, Scaramuzza, Harrer, Dietz, "Data Product MCP: Chat with your Enterprise Data", arXiv:2601.08687, 2026-01-13.** Agents as governed consumers of data products. Quote: "This data marketplace, already in use at large enterprises, enables AI agents to find, request, and query enterprise data products while enforcing data contracts in real time without lowering governance standards."
19. **Tamilselvan et al., "Agentic Control Center for Data Product Optimization", arXiv:2603.10133, 2026-03-10.** Agents improve data products. Quote: "We propose a system that automates data product improvement through specialized AI agents operating in a continuous optimization loop."
20. **Mishra et al., "An AI-Driven Data Mesh Architecture Enhancing Decision-Making in Infrastructure Construction and Public Procurement", arXiv:2412.00224, 2024-11-29.** Quote: "Our approach introduces an integrated software ecosystem utilizing Data Mesh and Service Mesh architectures."

**Near misses.** arXiv:2607.20488 (Sidik et al., "Autonomous Topology Mutation") uses "team topology" for the shape of an agent team: "Multi-agent LLM frameworks typically fix their team topology at boot time." It does not apply Skelton and Pais (citations not checked). The Conway's-law search returned arXiv:2604.01020, 2603.12229, 2607.25446 and 2609.14767 on organization of agent teams; their summaries name none of the three bodies of work, and they were not read.

**Pattern across E.** No source found organizes a system of agents with all three. The TT authors map team boundaries and cognitive load to agents and context windows, but keep the boundary with a human team. DDD blogs mostly equate one agent with one bounded context (Dinacode, Chauzov), the opposite of Dubrov's position recorded in the earlier reading. Data Mesh work mostly treats agents as consumers or builders of data products; only *Agentic Mesh* (unread) appears to apply mesh ideas to agents as the nodes.

[no-record: a peer-reviewed paper applying DDD context-map relationships, TT interaction modes or Data Mesh federated governance to the organization of LLM agents searched=arXiv API abstracts (queries above), six web searches, as of 2026-11-11; instrument confirmed able to return positives (it returned 2601.08687 and 2603.10133)]

---

## F. WARM sentences a reader of the three would ask to cite or narrow

1. "One test places a responsibility. **A responsibility belongs to the platform if it works the same whatever the work is about. It is domain work if what it does depends on the subject of the work.**" and "An older statement of the same idea is that the platform supplies mechanisms and a domain supplies meaning. The wording follows the separation of policy and mechanism in operating-system design (Levin ... 1975 ...)."
   Closer precedents in software architecture: DM-2019, "to not include any domain specific concepts or business logic, keeping it domain agnostic"; DDD Generic Subdomains, "Leave no trace of your specialties in them"; DDD Cohesive Mechanisms ("what" vs "how"). A reader would ask for these citations next to Hydra.
2. "A reusable responsibility discovered inside a domain is treated as a gap in the platform" and "A domain needs no platform service of its own. If it needs a reusable responsibility the platform lacks, that is a gap in the platform."
   DM-2019 states the same move: "Harvesting and extracting domain agnostic infrastructure capabilities into a data infrastructure platform solves the need for duplicating the effort".
3. "(The idea of a boundary around an area of work, inside which terms and rules have one meaning, is the bounded context of Domain-Driven Design.)"
   Evans's definition is "A description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable." It bounds a model, not an area of work. A reader would ask to quote Evans and narrow "area of work".
4. "In Domain-Driven Design a bounded context is a part of a system in which terms and rules have one agreed meaning (Evans, 2003)." (What WARM adds, item 2)
   The wording is Dubrov's ("a part of the system where business terms and rules have one agreed meaning"), attributed to Evans. Cite the Reference definition, or attribute the paraphrase.
5. "The survey found no source that puts domains of work in the same model as the platform. WARM joins them."
   Data Mesh puts domains, a self-serve platform and federated governance in one model (DM-2020, four principles). Team Topologies puts stream-aligned teams and platform teams in one model. Both are outside agent systems. A reader would ask to narrow the claim to models of agent systems, and to cite these as the general precedent.
6. "What WARM contributes is the whole in one picture. ... WARM puts the platform, the domains of work and the agents in one model, with a directory that records which domain is accountable for what".
   Same point as 5 for "platform and domains in one model".
7. "No source read has a directory of which domain is accountable for which responsibility, and AEON comes nearest." (What WARM adds, item 3)
   Near cases not listed: the DDD Context Map (a named record of all contexts and their relations); the TT Team API (per team: focus, owned software, services, contact channels); the Data Mesh catalogue ("a registry, a data catalogue, of all available data products with their meta information such as their owners"). None records accountability per responsibility, so the claim can stand, but these belong in the list of near cases.
8. "Domains depend on one another as the departments of an organization do. An agent in one asks an agent in another in ordinary language, the other uses its judgment, and the two sort out what was unclear."
   DDD's context-map relationships and TT's three interaction modes are published typologies of how such units relate. A reader would ask for a citation, and would note that both sources recommend a defined protocol or published language where WARM recommends ordinary language.
9. "An agent reaches a platform service differently: through a defined interface, with stated guarantees."
   TT's X-as-a-Service mode and DM-2019's "provides the data infrastructure components in a self-service manner" state the same relation.
10. "At that grain, exactly one domain is **accountable** for each responsibility." and "Two domains accountable for the same scoped responsibility is an overlap."
    DM-2020 states single accountability for data ("The accountability of data quality shifts upstream"). DDD's Shared Kernel deliberately shares a small part between two teams. A reader would ask whether a shared kernel counts as an overlap.
11. "Rules that authorize or forbid an action go to Policy and Approvals." and "the Communications domain supplies it, and the platform applies it."
    DM-2020: rules "defined by the global federated governance team, and automated by the platform", and access control "defined centrally but applied at the time of access". DDD Knowledge Level is a code-level precedent.
12. "Governance and Operations apply across the other groups." (organizing principles)
    Data Mesh's federated computational governance is a named precedent for governance across domains; WARM's Governance is services only and has no body that sets cross-domain rules.
13. "A builder who keeps each service behind a clear interface can change its supplier with less rework."
    DDD Pluggable Component Framework ("diverse implementations of those interfaces to be freely substituted") and Anticorruption Layer.
14. Glossary: "**Service** | Something the platform provides to agents in any domain ... Only the platform has services; a domain does work." and "**Domain** | An area of work ..."
    Both words have established, different meanings in DDD (domain service; domain as subject area) and TT (any team can provide "X-as-a-Service"). A reader who knows them would ask WARM to say it uses the words differently.

---

## G. What could not be read, and secondary quotes

Not read:
- Evans, *Domain-Driven Design* (2003 book). Only the 2015 Reference was read.
- Vernon, *Implementing Domain-Driven Design* (2013): source of the "supporting subdomain" classification. Not read.
- Skelton and Pais, *Team Topologies* (2019, 2nd ed. 2025): not available without purchase. The book's own definitions of the team types, interaction modes, platform, Team API (pp. 47-49 per the template) and TVP were not read. The key-concepts page is the authors' site but is written in a first-person voice ("I've seen ...") with no byline.
- Team Topologies "Executive Report: Team Topologies as The Organizational Foundation for AI ROI" (linked from the AI page): not opened.
- Dehghani, *Data Mesh* (O'Reilly, 2022): not read. Only the two martinfowler.com articles.
- Broda and Broda, *Agentic Mesh* (O'Reilly, 2026): O'Reilly returned 403; known from search summaries only.
- GitNation talk page and Gravitee corpus pages: fetches returned no article text.
- Figures in both Data Mesh articles and the TT key-concepts diagrams: images, read by caption only.

Secondary quotes in this file:
- Fowler, "TeamTopologies" bliki (https://martinfowler.com/bliki/TeamTopologies.html): the phrase "non-focal concerns" in 2B is Fowler's, not the authors'.
- InfoQ (item E4) reports Skelton's talk; the quotes are the reporter's words.
- wal.sh (E6) re-reads Wulveryck.
- QCon abstract (E13) is a conference description of Dehghani's talk, not her text.
- Nextdata (E14) is written by Cornelius Willis about a conversation with Dehghani.
- *Agentic Mesh* (E15) quotes come from search-result summaries of bookseller and publisher pages.
- Rework (E7) quotes Team Topologies key concepts as its source; its own sentences are quoted only where marked.

Extraction notes: the DDD Reference text was extracted from the PDF with pypdf. Two words split by the extraction ("t he", "t eam") are corrected in quotes; all other quotes are as extracted. Page numbers are the printed numbers with the PDF page in brackets.
