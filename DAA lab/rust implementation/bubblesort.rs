fn bubblesort<T>(data: &mut [T]) where T: Ord {
    for i in 0..data.len() - 1{
        let mut swapped = false;
        for j in 0..data.len() - i -1{
            if data[j] > data[j+1]{
                data.swap(j,j+1);
                swapped = true;
            }
        }
        if !swapped {
            break;
        }
    }
}

fn main() {
    let mut data = vec![64, 34, 25, 12, 22, 11];
    bubblesort(&mut data);
    
    println!("Sorted data: {:?}", data);
}
