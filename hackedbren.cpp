#include<bits/stdc++.h>
using namespace std;

void print_array(int arr[], int arr_size);
void delete_element(int arr[] ,int arr_size);
void insert_element(int arr[], int arr_size);
void sum_of_elements(int arr[], int arr_size);

int main()
{
	int n;
	cout<<"Enter the number of elements in your array: ";
	cin>>n;
	int arr[n];
	cout<<endl<<"Enter the elements of your array: ";
	
	for(int i = 0; i < n; i++)
	{	
		cin>>arr[i];
	}

	print_array(arr, n);

	n++;
	insert_element(arr, n);

	print_array(arr, n);

	delete_element(arr, n); 
	n--;

	print_array(arr, n);

	sum_of_elements(arr, n);


	return 0;
}

void print_array(int arr[], int arr_size)
{
	cout<<endl<<"Your array is:";

	for(int i = 0; i < arr_size; i++)
	{
		cout<<arr[i]<<" ";
	}
}

void delete_element(int arr[] ,int arr_size)
{
	int temp;
	jump_temp_del:
	cout<<endl<<"Enter position you want to delete element from: ";
	cin>>temp;
	if(temp > arr_size || temp < 0)
	{
		cout<<endl<<"Invalid position! Please select a valid position.";
		goto jump_temp_del;
	}

	arr_size = arr_size -1;
	while(temp < arr_size){
		arr[temp] = arr[temp + 1];
		temp += 1;
	}	
}

void insert_element(int arr[], int arr_size)
{
	int temp, tempval;
	jump_temp_ins:
	cout<<endl<<"Enter position you want to insert element to: ";
	cin>>temp;
	if(temp > arr_size+1 || temp < 0)
	{
		cout<<endl<<"Invalid position! Please select a valid position.";
		goto jump_temp_ins;
	}
	cout<<endl<<"Enter value of elemnent you want to insert: ";
	cin>>tempval;

	while(arr_size > temp)
	{
		arr[arr_size] = arr[arr_size - 1];
		arr_size--;
	}
	arr[temp] = tempval;
}

void sum_of_elements(int arr[], int arr_size)
{
	int sumans = 0;
	for(int i = 0; i < arr_size; i++)
	{
		sumans += arr[i];
	}
	cout<<endl<<"Sum of elements of the array is: "<<sumans;
}
