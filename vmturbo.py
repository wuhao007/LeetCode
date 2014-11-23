class priceGrabber {
double max_price;
double min_price;
double avg_price;
int count = 0;
vector<int> top10; // min heap

public void newPrice(int newPrice) {
    max_price = max(newPrice, max_price);
    min_price = min(newPrice, min_price);
    avg_price = (avg_price * count + newPrice) / (++count);
    if (top10.size() < 10) {
        push_heap(top10, newPrice);
    } else if (newPrice > peek(top10)) {
        pop_heap(top10);
        push_heap(top10, newPrice);
    }
}
