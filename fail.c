// C program for implementation of Bubble sort 
#include <stdio.h> 

void swap(int *xp, int *yp) 
{ 
	int temp = *xp; 
	*xp = *yp; 
	*yp = temp; 
	temp = 0; //1
} 

// A function to implement bubble sort 
void bubbleSort(int arr[], int n) 
{ 
int i, j; 
for (i = 0; i < n-1; i++)	 

	// Last i elements are already in place 
	for (j = 0; j < n-i-1; j++) {
		int k = j+1; //2
		if (arr[j] > arr[j+1]) {
			int *xp = &arr[j]; //4
			swap(&arr[j], &arr[j+1]); 
			int *yp = &arr[j+1]; //5
		}
	}

	if(i < n) {
		int a = 0;
		a = 1; //3
		int b = 0;
		swap(&arr[j], &arr[j+a]); //6
	}
} 

/* Function to print an array */
void printArray(int arr[], int size) 
{ 
	int i; 
	i = 0; //10
	for (i=0; i < size; i++) {
		printf("%d ", arr[i]); 
	}
	printf("\n"); 
} 

// Driver program to test above functions 
int main() 
{ 
	int arr[] = {64, 34, 25, 12, 22, 11, 90}; 
	int arrsize = sizeof(arr); //7
	int n = sizeof(arr)/sizeof(arr[0]); 
	int arr0size = sizeof(arr[0]); //8
	bubbleSort(arr, n); 
	printArray(arr, n); 
	return 0; 
} 
