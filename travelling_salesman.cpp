#include<bits/stdc++.h>
using namespace std;
#define p pair<bool,int>
#define f first
#define s second

int ncities;
vector<bool>visited;
vector<int>f;
vector<int>g;
vector<int>h;
vector<vector<int>>citygraph;

//Initializing f = totalcost, g = actual cost , h = heuristic cost;
void init() {
	f.resize(ncities,INT_MAX);
	g.resize(ncities,INT_MAX);
	h.resize(ncities, INT_MAX);
	citygraph.resize(ncities, vector<int>(ncities, 0));
}

//Taking input and Building Adjacency Matrix for The city graph
void buildgraph() {
	cout<<"Enter the distance between cities"<<"\n";
	for(int i=0;i<ncities;i++) {
		for(int j = 0;j<ncities;j++) {
			if(i == j) {citygraph[i][j] = 0; continue;}
			cout<<i<<" --> "<<j<<" : ";
			cin>>citygraph[i][j];
			cout<<"\n";
		}
	}
}

//Class Representing the State of city at a given time in astar traversal.
class State {
	public :
		int totalcost;
		int citynum;
		vector<bool> visited;
		vector<int> path_travelled;

		bool operator <(const State& op2) const {
			return this->totalcost < op2.totalcost;
		}

		State(int citynum) {
			visited.resize(ncities, false);
			this->citynum = citynum;
			visited[citynum] = true;
			this->totalcost = 0;
		}
		State(int citynum, int totalcost) {
			visited.resize(ncities, false);
			this->citynum = citynum;
			this->totalcost = totalcost;
			visited[citynum] = true;
		}
		State(int citynum, int totalcost, vector<bool> visited, vector<int> path_travelled) {
			this->visited = visited;
			this->citynum = citynum;
			this->totalcost = totalcost;
			this->path_travelled = path_travelled;
			visited[citynum] = true;

		}
};

//Getting heuristic value for a given city
int get_heuristic(int start, int citynum, State state) {

	// Heuristic used is ::
	// Length of smallest unused edge leaving current node + length of smallest
	// unused edge entering start node

	int allcityvisited = true;;
	int min_unused = INT_MAX;
	for(int i=0; i<citygraph[citynum].size(); i++) {
		if(not state.visited[i]) {
			allcityvisited = false;
			min_unused = min(min_unused, citygraph[citynum][i]);
		}
	}
	int min_unused_start = INT_MAX;
	for(int i=start;i<citygraph[start].size(); i++) {
		if(not state.visited[i]) {
			min_unused_start = min(min_unused_start, citygraph[start][i]);
		}
	}
	if(allcityvisited) return 0;
	return min_unused_start + min_unused;
}

//Checking if goal is reached - if all cities are visited, the it a goal states.
bool isgoal(State &currstate, int startcity) {
	
	bool allcityvisited = true;
	for(int vis : currstate.visited) {
		if(not vis) {
			allcityvisited = false;
			break;
		}
	}
	return allcityvisited;
}

//Astar Search
State astar(int start) {
	//Getting costs for initial state.
	h[start] = get_heuristic(start, start, State(start));
	g[start] = 0;
	f[start] = g[start] + h[start];

	multiset<State> pq;
	State startstate = State(start, f[start]);
	startstate.visited[start] = true;
	startstate.path_travelled.push_back(start);

	pq.insert(startstate);

	while(not pq.empty()) {
		State currstate = *pq.begin();
		pq.erase(currstate);
		if(isgoal(currstate, start)) {pq.clear(); return currstate;} //Check for goal state.

		for(int i=0;i<citygraph[currstate.citynum].size();i++) {
			// if(g(u) + d(u,v) < g(v)) then g(v) = g(u) + d(u,v)
			if(g[currstate.citynum] + citygraph[currstate.citynum][i] < g[i]) {
				g[i] = g[currstate.citynum] + citygraph[currstate.citynum][i];

				State nxtstate = State(i, g[i], currstate.visited, currstate.path_travelled);
				nxtstate.visited[i] = true;
				nxtstate.path_travelled.push_back(i);
				h[i] = get_heuristic(start, i, nxtstate);
				f[i] = g[i] + h[i];                       //Estimated Total Cost for neighbour node
				nxtstate.totalcost = f[i];

				//Check if neighbour node is present in PriorityQueue
				multiset<State>::iterator it = pq.begin();
				bool inPriorityQueue = false;
				while(it != pq.end()) {
					if(it->citynum == i) {
						inPriorityQueue = true;
						break;
					}
					++it;
				}

				//Decrease Key if neighbour node is present in PriorityQueue
				if(not inPriorityQueue) pq.insert(nxtstate);
				else {
					pq.erase(*it);
					pq.insert(nxtstate);
				}

			}
		}
	}

}


int main() {
	cout<<"Enter the number of cities."<<endl;
	cin>>ncities;
	init();
	buildgraph();
	State goalState = astar(0);
	int optimum_cost = goalState.totalcost;
	cout<<"Optimum Cost = "<<optimum_cost<<endl;
	vector<int> path = goalState.path_travelled;

	cout<<"Optimum Path is ::"<<endl;
	for(int city : path) cout<<city<<" --> ";
	cout<<endl;
}
