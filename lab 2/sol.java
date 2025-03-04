import java.util.ArrayList;
import java.util.Random;

public class Main {

    public static void Swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    public static int Shell_Sort(int[] arr, int[] steps) {
        int cnt = 0;
        for (int step : steps) {
            for (int j = step; j < arr.length; j++) {
                int i = j;
                while (i >= step && arr[i - step] > arr[i]) {
                    Swap(arr, i, i - step);
                    i -= step;
                    cnt++;
                }
                cnt++;
            }
        }
        return cnt;
    }

    public static int BubbleSort (int[] arr) {
        int cnt = 0;
        for (int i = 0;i < arr.length-1;++i) {
            for(int j = 0;j < arr.length - i - 1;++j) {
                if (arr[j] > arr[j+1]) {
                    Swap(arr,j,j+1);
                }
                cnt++;
            }
        }
        return cnt;
    }

    public static ArrayList<Integer> setSteps(int n) { // последовательность Седжвика
        int step = 0;

        int i = 0;
        ArrayList<Integer> steps = new ArrayList<>();
        while (step < n) {
            if (i % 2 == 0) {
                step = (9 * (int) Math.pow(2, i) - 9 * (int) Math.pow(2, (double) i / 2)) + 1;
            } else {
                step = (8 * (int) Math.pow(2, i) - 6 * (int) Math.pow(2, (double) (i + 1) / 2)) + 1;
            }

            if (step < n) {
                steps.addFirst(step);
            }
            i++;
        }
        return steps;
    }

    public static void main(String[] args) {
        int n = 100;
        ArrayList<Integer> stepss = setSteps(n);
        int[] steps = stepss.stream().mapToInt(Integer::intValue).toArray();
        System.out.println("Массив шагов:");
        for (int i : steps) {
            System.out.print(i + " ");
        }
        System.out.println("\nИзначальный массив данных:");
        int[] b = new int[n];
        Random rand = new Random();
        for (int j = 0; j < b.length; ++j) {
            b[j] = rand.nextInt(100);
        }
        for (int i : b) {
            System.out.print(i + " ");
        }
        int[] b1 = b.clone();
        int cnt = Shell_Sort(b, steps);
        System.out.println("\nМассив отсортирован Шеллом за " + cnt + " сравнений");
        for (int i : b) {
            System.out.print(i + " ");
        }
        cnt = BubbleSort(b1);
        System.out.println("\nМассив отсортирован Пузырьком за " + cnt + " сравнений");
        for (int i : b1) {
            System.out.print(i + " ");
        }
    }

}
