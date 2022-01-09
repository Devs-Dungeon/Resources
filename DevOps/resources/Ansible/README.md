# Ansible

<p align="center"><img  width="150" height="150" src="https://i.ibb.co/P9KZg3c/ansi.png"></p>

Ansible is an open-source software provisioning, configuration management, and application-deployment tool enabling infrastructure as code. It runs on many Unix-like systems, and can configure both Unix-like systems as well as Microsoft Windows :computer:

- [Cheat Sheet](https://www.edureka.co/blog/wp-content/uploads/2018/11/Ansible-Cheat_Sheet_Edureka.pdf)

## Getting Started :pushpin:

- [Ansible Docs](https://docs.ansible.com/)
- [Why you need to start Ansible Right now](https://www.youtube.com/watch?v=5hycyr-8EKs)
- [What is Ansible](https://www.youtube.com/watch?v=4nKW2eF-nIw)
- [One of the Best Channels](https://www.youtube.com/channel/UCR-DXc1voovS8nhAvccRZhg)

## Courses :blue_book:

- [Ansible for Beginners](https://www.udemy.com/course/learn-ansible/)
- [Advanced Ansible](https://www.udemy.com/course/learn-ansible-advanced/)
- [Ansible for Network Engineers](https://www.udemy.com/course/ansible-for-network-engineers-cisco-quick-start-gns3-ansible/)
- [Playbooks Deep Dive](https://linuxacademy.com/redirect/LA_COURSE_318)
- [Red Hat Certified Ansible Specialist Training](https://linuxacademy.com/redirect/LA_COURSE_198)
- [Ansible from Ground Up](https://www.eduonix.com/learn-ansible-from-ground-up-the-devops-guide)

## Topics to Follow :fountain_pen:

| S.No | Topic            | Link                                                                                                                                               |
| ---- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Ad Hoc Commands  | [Link](https://www.howtoforge.com/ansible-guide-ad-hoc-command/)                                                                                   |
| 2    | Playbooks        | [Link](https://www.tothenew.com/blog/understanding-playbooks-in-ansible/)                                                                          |
| 3    | Variables        | [Link](https://www.tecmint.com/ansible-variables-and-facts/)                                                                                       |
| 4    | Block and Rescue | [Link](https://docs.ansible.com/ansible/2.4/playbooks_blocks.html)                                                                                 |
| 5    | Loops            | [Link](https://www.linuxtechi.com/how-to-use-loops-in-ansible-playbook/)                                                                           |
| 6    | Templating       | [Link](https://www.toptechskills.com/ansible-tutorials-courses/ansible-template-module-tutorial-examples/)                                         |
| 7    | Vaults           | [Link](https://www.digitalocean.com/community/tutorials/how-to-use-vault-to-protect-sensitive-ansible-data-on-ubuntu-16-04)                        |
| 8    | Roles and Galaxy | [Link](https://www.tutorialspoint.com/ansible/ansible_roles.htm#:~:text=Roles%20provide%20a%20framework%20for,makes%20them%20easier%20to%20reuse.) |

## Companies using Ansible

- Red Hat
- IBM
- Wells Fargo
- Lockheed Martin
- SOLUTE
- Apple
- NASA
- Atlassian
- Siemens

## Repositories and people to follow :star:

- [Official Ansible Repository](https://github.com/ansible/ansible)
- [Best Guy for Ansible](https://github.com/geerlingguy)
- [Ansible for Devops](https://github.com/geerlingguy/ansible-for-devops)
- [Ansible Examples](https://github.com/ansible/ansible-examples)
- [Working with Containers](https://github.com/ansible/ansible-container)

<hr>

### Learn Ansible

Name | Comments
:------ |:--------:
[Ansible 101 - Jeff Geerling](https://www.youtube.com/watch?v=goclfp6a2IQ&list=RDCMUCR-DXc1voovS8nhAvccRZhg&index=1) | Comprehensive practical way to learn Ansible
[What is Ansible? - TechWorld with Nana](https://www.youtube.com/watch?v=1id6ERvfozo) | High-level short overview of Ansible
[Learning Ansible basics - Red Hat](https://www.redhat.com/en/topics/automation/learning-ansible-tutorial) | Red Hat's guide on how to learn Ansible basics + links to the content itself
[Introduction to Ansible - 2021](https://medium.com/@bagusays/introduction-to-ansible-82f2bc12cd87) |

### Articles

Name | Comments
:------ |:--------:
[Writing reliable Ansible Playbooks - 2021](https://dev.to/xlab_si/writing-reliable-ansible-playbooks-295i) | 
[A CI/CD Pipeline Project for a Trunk-Based Development Strategy in a Kubernetes Environment](https://medium.com/swlh/a-ci-cd-pipeline-project-for-a-trunk-based-development-strategy-in-a-kubernetes-environment-c4ffea9700fe) |

### Books

Name | Comments
:------ |:--------:
[Ansible for DevOps](https://www.amazon.com/Ansible-DevOps-Server-configuration-management/dp/098639341X) | 
[Ansible: From Beginner to Pro](https://www.amazon.com/Ansible-Beginner-Pro-Michael-Heap/dp/1484216601) |
[Ansible: Up and Running](https://www.amazon.com/Ansible-Automating-Configuration-Management-Deployment/dp/1491979801) |


### Cheat Sheet

* Check if list has elements

```
when: my_list | length > 0
```

* Update all packages

```
- name: Update system packages
  package:
    state: latest
    name: "*"
```

* Update packages informations and display packages informations

```
- name: Update packages informations
  package_facts:
    manager: "auto"

- name: Display all installed packages informations
  debug:
    msg: "{{ ansible_facts.packages }}"

- name: Display all Chromium package informations
  debug:
    msg: "{{ ansible_facts.packages['chromium'] }}"
  when: "'chromium' in ansible_facts.packages"
```

We hope you now know the roadmap to being a professional Ansible Developer :v: