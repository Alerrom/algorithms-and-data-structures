n = int(input())
 
data = list(map(int, input().split()))
m_len = [0 for i in range(n)]
 
for k in range(n):
    m_len[k] = 1
    for i in range(k):
        if data[i] < data[k]:
            m_len[k] = max(m_len[k], m_len[i]+1)
 
m_ind = 0
m_val = m_len[0]
 
for i in range(1, n):
    if m_val < m_len[i]:
        m_val = m_len[i]
        m_ind = i
         
print(m_val)
print(*data[m_ind - m_val + 1 : m_ind + 1])
    
