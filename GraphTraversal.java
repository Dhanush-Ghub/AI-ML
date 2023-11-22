import java.util.*;

public class GraphTraversal {

    public static List<Integer> bfsAdjMatrix(int[][] adjMatrix, int startNode, int numNodes) {
        // Perform BFS traversal for Adjacency Matrix
        boolean[] visited = new boolean[numNodes];
        List<Integer> traversalOrder = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.add(startNode);
        visited[startNode] = true;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            traversalOrder.add(current);

            for (int i = 0; i < numNodes; i++) {
                if (adjMatrix[current][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
        return traversalOrder;
    }

    public static List<Integer> dfsAdjMatrix(int[][] adjMatrix, int startNode, int numNodes) {
        // Perform DFS traversal for Adjacency Matrix
        boolean[] visited = new boolean[numNodes];
        List<Integer> traversalOrder = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(startNode);

        while (!stack.isEmpty()) {
            int current = stack.pop();
            if (!visited[current]) {
                traversalOrder.add(current);
                visited[current] = true;
                for (int i = 0; i < numNodes; i++) {
                    if (adjMatrix[current][i] == 1 && !visited[i]) {
                        stack.push(i);
                    }
                }
            }
        }
        return traversalOrder;
    }

    public static List<Integer> bfsAdjList(Map<Integer, List<Integer>> adjList, int startNode) {
        // Perform BFS traversal for Adjacency List
        Set<Integer> visited = new HashSet<>();
        List<Integer> traversalOrder = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.add(startNode);
        visited.add(startNode);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            traversalOrder.add(current);

            for (int neighbor : adjList.get(current)) {
                if (!visited.contains(neighbor)) {
                    queue.add(neighbor);
                    visited.add(neighbor);
                }
            }
        }
        return traversalOrder;
    }

    public static List<Integer> dfsAdjList(Map<Integer, List<Integer>> adjList, int startNode) {
        // Perform DFS traversal for Adjacency List
        Set<Integer> visited = new HashSet<>();
        List<Integer> traversalOrder = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(startNode);

        while (!stack.isEmpty()) {
            int current = stack.pop();
            if (!visited.contains(current)) {
                traversalOrder.add(current);
                visited.add(current);
                for (int neighbor : adjList.get(current)) {
                    if (!visited.contains(neighbor)) {
                        stack.push(neighbor);
                    }
                }
            }
        }
        return traversalOrder;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("Case 1: Graph representation by Adjacency Matrix");
            System.out.println("Case 2: Graph representation by Adjacency List");
            System.out.println("Case B/b: BFS Traversal");
            System.out.println("Case D/d: DFS Traversal");
            System.out.println("Case T/t: Both BFS and DFS traversal");
            System.out.println("Case X/x: Exit");

            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter the number of nodes: ");
                int numNodes = scanner.nextInt();
                int[][] adjMatrix = new int[numNodes][numNodes];

                for (int i = 0; i < numNodes; i++) {
                    System.out.print("Enter connections for node " + i + " (0 or 1): ");
                    for (int j = 0; j < numNodes; j++) {
                        adjMatrix[i][j] = scanner.nextInt();
                    }
                }

                System.out.print("Enter the starting node for traversal: ");
                int startNode = scanner.nextInt();

                System.out.print("Choose B/b for BFS or D/d for DFS: ");
                String traversalChoice = scanner.next();

                List<Integer> traversalOrder;
                if (traversalChoice.equalsIgnoreCase("B")) {
                    traversalOrder = bfsAdjMatrix(adjMatrix, startNode, numNodes);
                } else if (traversalChoice.equalsIgnoreCase("D")) {
                    traversalOrder = dfsAdjMatrix(adjMatrix, startNode, numNodes);
                } else {
                    System.out.println("Invalid choice");
                    continue;
                }

                System.out.println("Order of traversal: " + traversalOrder);
            } else if (choice.equals("2")) {
                // Implement Adjacency List input and traversal similarly to Adjacency Matrix
                System.out.println("Adjacency List traversal will be implemented next.");
            } else if (choice.equalsIgnoreCase("X")) {
                System.out.println("Exiting...");
                break;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
