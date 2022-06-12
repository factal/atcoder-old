// -*- coding:utf-8-unix -*-

use proconio::input;
use proconio::marker::Usize1;
use petgraph::unionfind::UnionFind;

fn main() {
    input! {
        n: usize,
        m: usize,
        mut set: [(Usize1, Usize1); m]
    }

    let mut list = vec![vec![]; n];
    let mut uf = UnionFind::new(n);
    for (a, b) in set {
        list[a].push(b);
        list[b].push(a);
        if uf.equiv(a, b) {
            println!("No");
            return;
        } else {
            uf.union(a, b);
        }
    }

    for i in list {
        if i.len() >= 3 {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
