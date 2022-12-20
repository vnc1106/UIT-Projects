Bài này mình có thể can thiệp và chỉnh sửa thông tin trao đổi giữa Alice và Bob.

Alice sẽ sinh ra bộ khóa (g, a, p), tính A = g^a (mod p) và gửi (A, g, p) cho Bob. Bob sẽ chọn ngẫu nhiên b và tính B = g^b (mod p) và gửi B lại cho Alice. Vậy Alice sẽ tính shared_key = B^a = g^(a*b) (mod p).

Ý tưởng là mình sẽ can thiệp và sửa lại B = 1, khi đó rõ ràng không cần biết a, chắc chắn Alice sẽ tính ra shared_key = B^a = 1 (mod p). Có shared_key => xong!