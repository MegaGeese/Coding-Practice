class App {
    public boolean checkPerfectNumber(int num) {
        int sum = 0;
        for(int i = 1; i < num / 2; i++){
            if(num % i == 0){
                sum += i;
            }
        }
        if (sum == num){
            return true;
        }
        int[] x = {6, 28, 496, 8128, 33550336};
        int y = x.length;
        return false;
    }
}