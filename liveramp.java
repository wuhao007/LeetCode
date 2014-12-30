public class liveramp {
    public static void main(String[] args) {
        int[] arr = new int[] {3, 7, 1, 11, 5};
        int i = 0, j = arr.length - 1;
        while (i <= j) {
            i++;
            if (i == j) {
                System.out.println(arr[i]);
//                return arr[i];
            }
            j--;
        }
        System.out.println(arr[i]);
//return arr[i];
    }
}
