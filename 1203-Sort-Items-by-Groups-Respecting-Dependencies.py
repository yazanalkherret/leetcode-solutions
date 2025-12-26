# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_members = defaultdict(list)
        group_assignment_counter = m
        
        for i, group_code in enumerate(group):
            if group_code == -1:
                group[i] = group_assignment_counter
                group_assignment_counter += 1

            group_members[group[i]].append(i)

        group_adj = defaultdict(list)
        num_groups = group_assignment_counter
        group_degree = [0] * num_groups

        # Top-sort groups
        
        for i in range(n):
            for dependency in beforeItems[i]:
                dependent_group = group[i]
                if group[dependency] != dependent_group:
                    group_adj[group[dependency]].append(group[i])
                    group_degree[group[i]] += 1

        group_queue = deque()
        for i, degree in enumerate(group_degree):
            if not degree:
                group_queue.append(i)

        group_order = []
        while group_queue:
            curr_group = group_queue.popleft()
            group_order.append(curr_group)

            for next_group in group_adj[curr_group]:
                group_degree[next_group] -= 1
                if not group_degree[next_group]:
                    group_queue.append(next_group)

        if len(group_order) != num_groups: return []
        
        # Top-sort items

        item_degree = [0] * n
        item_adj = defaultdict(list)

        for i in range(n):
            for dependency in beforeItems[i]:
                item_adj[dependency].append(i)
                item_degree[i] += 1

        item_order = []
        item_queue = deque()

        for grp in group_order:
            for item in group_members[grp]:
                if not item_degree[item]:
                    item_queue.append(item)

            while item_queue:
                curr_item = item_queue.popleft()
                item_order.append(curr_item)

                for next_item in item_adj[curr_item]:
                    item_degree[next_item] -= 1
                    if not item_degree[next_item] and group[next_item] == group[curr_item]:
                        item_queue.append(next_item)

        return item_order if len(item_order) == n else []
