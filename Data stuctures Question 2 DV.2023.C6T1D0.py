import networkx as nx
import matplotlib.pyplot as plt

class ConnectionsManager:
    def __init__(self):
        self.graph = nx.Graph()  # Initialize an empty graph
    
    def add_user(self, user):
        """Add a user (node) to the graph."""
        if user not in self.graph:
            self.graph.add_node(user)
            print(f"User '{user}' added successfully.")
        else:
            print(f"User '{user}' already exists.")
    
    def add_connection(self, user1, user2):
        """Add a connection (edge) between two users."""
        if user1 in self.graph and user2 in self.graph:
            self.graph.add_edge(user1, user2)
            print(f"Connection between '{user1}' and '{user2}' added successfully.")
        else:
            print("One or both users do not exist. Add them as users first.")
    
    def view_all_users(self):
        """View all users in the network."""
        if len(self.graph.nodes) > 0:
            print("All Users:")
            for user in self.graph.nodes:
                print(f" - {user}")
        else:
            print("No users in the network.")
    
    def view_all_connections(self):
        """View all connections in the network."""
        if len(self.graph.edges) > 0:
            print("All Connections:")
            for user1, user2 in self.graph.edges:
                print(f" - {user1} <--> {user2}")
        else:
            print("No connections in the network.")
    
    def display_graph(self):
        """Display the graph visually."""
        if len(self.graph.nodes) > 0:
            plt.figure(figsize=(8, 6))
            nx.draw(self.graph, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_weight="bold", edge_color="gray")
            plt.title("Social Network Connections")
            plt.show()
        else:
            print("No users in the network to display.")

def main_menu():
    manager = ConnectionsManager()
    
    while True:
        print("\nSocial Media Connections Manager")
        print("1. Add User")
        print("2. Add Connection")
        print("3. View All Users")
        print("4. View All Connections")
        print("5. Display Graph")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            user = input("Enter the username to add: ")
            manager.add_user(user)
        
        elif choice == '2':
            user1 = input("Enter the first username: ")
            user2 = input("Enter the second username: ")
            manager.add_connection(user1, user2)
        
        elif choice == '3':
            manager.view_all_users()
        
        elif choice == '4':
            manager.view_all_connections()
        
        elif choice == '5':
            manager.display_graph()
        
        elif choice == '6':
            print("Exiting the Social Media Connections Manager.")
            break
        
        else:
            print("Invalid option. Please select a number between 1 and 6.")

# Run the application
if __name__ == "__main__":
    main_menu()
