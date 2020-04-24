/* Snippet */

#define NUM_FUNCS 3

int func1(int arg)
{
	return 1+arg;
}

int func2(int arg)
{
	return 2+arg;
}

int func3(int arg)
{
	return 3+arg;
}

static int (*funcList[NUM_FUNCS]) (int arg) =
{
	func1,
	func2,
	func3,
};

int main(void)
{
	int retVal, argIn, i;

	for (i = 0; i < NUM_FUNCS; i++)
	{
		retVal += (*funcList[i]) (argIn)
	}

	return retVal;
}

/* End snippet */