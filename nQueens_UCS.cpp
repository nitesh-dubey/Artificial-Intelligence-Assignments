#include <bits/stdc++.h>
#define vecint vector<int>
#define priorityQueue priority_queue<cell, vector<cell>, cmp>
using namespace std;

struct cell{
	vecint states;
	int cost;
	int next_cell;
};

struct cmp{
	bool operator()(cell c1, cell c2){
		return c1.cost < c2.cost;
	}
};

bool is_safe(vecint cur_states, int row, int col){
	bool flag = true;
	for(int i=0; i<cur_states.size(); i++){
		if(cur_states[i] == row || abs(cur_states[i]-row) == abs(col-i)){
			flag = false; break;
		}
	}
	return flag;
}

cell get_new_cell(cell value, int next_row){
	vecint v;
	if(value.states.size()){
		v.assign(value.states.begin(), value.states.end());
	}
	v.push_back(next_row);
	cell new_cell;
	new_cell.states = v;
	new_cell.cost = value.cost;
	new_cell.next_cell = v.size();
	return new_cell;
}

bool is_goal(vecint v){
	bool flag = true;
	for(int i=0; i<v.size(); i++){
		for(int j=0; j<v.size(); j++){
			if(i==j) continue;
			if(v[i] == v[j] || abs(v[i]-v[j]) == abs(i-j)){
				flag = false; break;
			}
		}
	}
	return flag;
}

void print_goal(vecint v){
	cout << "[ ";
	for(auto i : v){
		cout << i << " ";
	}
	cout << "]\n";
}

int total_states = 0;

void uniform_cost_search(priorityQueue pq, int n){
	int next_first_cell = 1;          // if the pqueue.empty(), next_first_cell stores 
									  // the row no. from where to start ucs next
	while(true){
		cell value;
		if(pq.size()){
			value = pq.top();
			pq.pop();
		}
		else{
			if(next_first_cell == n) return;
			value.states.push_back(next_first_cell++);
			value.cost = 0;              // if pqueue.empty(), making value to be the next cell
			value.next_cell = 1;
		}
		if(value.states.size() == n){
			if(is_goal(value.states)){
				total_states++;
				print_goal(value.states);
			}
			continue;
		}
		for(int i=0; i<n; i++){
			if(is_safe(value.states, i, value.next_cell)){
				cell new_cell = get_new_cell(value, i);
				pq.push(new_cell);
			}
		}
	}
}

int main(){
	int n;
	cout<<"Enter the value of n :  ";
	cin>>n;
	priorityQueue pq;
	cell first;
	first.states.push_back(0);    // pushing '0' = placing the queen at (0,0) of the board
	first.cost = 0;      		  // g(0) = 0
	first.next_cell = 1;          // next_cell = row where next queen is placed
	pq.push(first);

	uniform_cost_search(pq,n);

	cout << "total states = " << total_states<<endl;
}