class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.resources = {}
        
    def add_task(self, task_id, name, dependencies, duration, resources_needed):
        # ISSUE: No input validation
        self.tasks[task_id] = {
            'name': name,
            'dependencies': dependencies,
            'duration': duration,
            'resources': resources_needed,
            'start_date': None
        }
        
    def detect_circular_dependencies(self):
        # ISSUE: Inefficient O(n²) algorithm, doesn't handle all cases
        for task_id in self.tasks:
            visited = []
            if self._has_cycle(task_id, visited):
                return True
        return False
        
    def _has_cycle(self, task_id, visited):
        # ISSUE: Incorrect cycle detection logic
        if task_id in visited:
            return True
        visited.append(task_id)
        for dep in self.tasks[task_id]['dependencies']:
            if self._has_cycle(dep, visited):
                return True
        return False
        
    def calculate_earliest_start(self, task_id):
        # ISSUE: No memoization, exponential time complexity
        if not self.tasks[task_id]['dependencies']:
            return 0
        max_end = 0
        for dep in self.tasks[task_id]['dependencies']:
            dep_start = self.calculate_earliest_start(dep)
            dep_end = dep_start + self.tasks[dep]['duration']
            max_end = max(max_end, dep_end)
        return max_end