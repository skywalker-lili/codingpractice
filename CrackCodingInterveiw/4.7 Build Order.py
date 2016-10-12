
# coding: utf-8

# In[12]:


# 4.7 Build Order
        
# Solution 1: topological sort
# Helper function to build a graph
def build_dependency(dependency, relation):
    """
    Add relation into dependency
    """
    prereq = relation[0]
    proj = relation[1]
    
    if proj in dependency.keys():
        dependency[proj].append(prereq)
    else:
        dependency[proj] = [prereq]

def build_order_topology(projects, relations):
    """
    Give some relations, output a possible order of build orders
    """
    # Build dependency
    dependency = {}
    for relation in relations:
        build_dependency(dependency, relation)
    
    # Find projects that doesn't depend on any one, add them to
    # a list of workable projects
    workable = []
    for p in projects:
        if p not in dependency:
            workable.append(p)
    
    # Now can do the workable projects
    # Remove them from workable, add to build order
    # At the same time, remove the dependencies on them in the dependency
    # Keep doing this until workable is empty
    done = []
    while len(workable) > 0:
        # Move a project from workable to done 
        proj = workable.pop()
        done.append(proj)
        
        # Update the dependencies
        for p, dep in dependency.items():
            if proj in dep:
                dep.remove(proj)
            if len(dep) == 0: # if this project doesn't depend on anything
                dependency.pop(p) # remove it from dependency
                workable.append(p) # add it to workable
    
    # When stop check if the done list contains all projects
    # If not, some project can't be done, return an Error
    if len(done) != len(projects):
        print("No such a building order")
        return done
    else:
        return done

    
# Solution 2: DFS
# Helper function to do dfs
def DFS(project, dependency, done, visited_inThisDFS):
    """
    Do DFS on a project and add it and nodes in its DFS route in the correct order.
    """
    if project in done: # if project is already DFSed
        return True
    
    if project not in dependency: # this project doesn't depend on any other project
        done.append(project)
        return True
    
    visited_inThisDFS.add(project)
    for dependent in dependency[project]:
        if dependent in visited_inThisDFS: # a child is already DFS in this round, must be a circle!
            return False
        else:
            DFS(dependent, dependency, done,visited_inThisDFS)
    
    done.append(project)
    return True

def build_order_DFS(projects, relations):
    """
    DFS from all nodes. When a DFS ends, the end node must have no dependents so can be done.
    Problem 1: notice that there could be loop and DFS won't stop. Use a state to record this
    Problem 2: when a node is done, no need to dfs it again. Use a state to record this
    """
    # Build dependency
    dependency = {}
    for relation in relations:
        build_dependency(dependency, relation)
    
    # DFS each projects
    done = []
    visited_inThisDFS = set([])
    for project in projects:
        res = DFS(project, dependency, done, visited_inThisDFS)
        if res == False:
            print("Contains a circle. Build order can't be made!")
            return []
        visited_inThisDFS = set([]) # reset the set before a new DFS starts
    
    return done


# In[14]:

# Test 
projects = ["a","b","c","d","e","f"]
dependencies = [("a", "d"),  ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
print(build_order_topology(projects, dependencies), build_order_DFS(projects, dependencies))


# In[1]:



