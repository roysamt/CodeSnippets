# Snippet

##-- us2s(usv, bits) - Convert unsigned int to signed int -> usv = unsigned int, sv = signed int --## 
def us2s(usv, bits):
  #bits = 16 for uint16, etc
  sv = 0 
  if usv < (1 << bits-1):
    sv = usv 
  else:
    sv = usv - (1 << bits)
  return sv

##-- s2us(sv, bits) - Convert signed int of size "bits" to unsigned int of same size --## 
def s2us(sv, bits):
  #bits = 16 for uint16, etc
  usv = 0 
  usv = sv + (1 << bits)
  return usv

##-- e2s(msb, lsb) - Convert eight bit int LSB and MSB to single sixteen bit int --## 
def e2s(msb, lsb): 
  ret = (msb << 8) | lsb
  return ret

##-- e2l(msb1, b2, b3, lsb4) - Convert eight bit ints to single 32 bit int --## 
def e2l(msb1, b2, b3, lsb4): 
  ret = (msb1 << 24) | (b2 << 16) | (b3 << 8) | lsb4
  return ret

##-- e2ll(msb1, b2, b3, b4, b5, b6, b7, lsb8) - Convert eight bit ints to single 64 bit int --##
def e2ll(msb1, b2, b3, b4, b5, b6, b7, lsb8): 
  ret = (msb1 << 56) | (b2 << 48) | (b3 << 40) | (b4 << 32) | (b5 << 24) | (b6 << 16) | (b7 << 8) | lsb8
  return ret

# End snippet