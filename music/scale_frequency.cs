using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Music {
    static Dictionary<string, int> d = new Dictionary<string, int>();
    static string[] chars = new string[]{"c", "d", "e", "f", "g", "a", "b"};
    static int[] l = new int[]{1, 2, 2, 1, 2, 2, 2};

    private static int inner(int acc, Tuple<string, int> t){
        acc += t.Item2;
        d[t.Item1] = acc;
        return acc;
    }

    private static bool fill(string k, int v){
        d.Add(k, v);
        return true;
    }

    static void test(){
        IEnumerable<Tuple<string, int>> v1 = from i in Enumerable.Range(1, 3)
                                          from j in Enumerable.Range(0, 7)
                                          where fill(chars[j]+i, l[j])
                                          select Tuple.Create(chars[j]+i, l[j]);

        v1.ToList().Aggregate(-1, inner);
        Console.WriteLine(d["a1"] - d["e1"]);
    }

    public static void Main(){
        test();
        Console.WriteLine("ok");
    }
}
