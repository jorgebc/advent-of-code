def translateNumberToDecimal(snafu):

  numbers = [number for number in snafu]
  numbers.reverse()

  decimal = 0

  for position in range(len(numbers)): 
    patata = pow(5, position)

    snafuNumber = numbers[position]
    if snafuNumber == '-': snafuNumber = "-1"
    if snafuNumber == '=': snafuNumber = "-2"

    decimal += int(snafuNumber)*patata

  return decimal

def translateNumbersToDecimal(snafuNumbers):
  numbers = snafuNumbers.split("\n")
  decimalNumbers = []

  for number  in numbers:
    decimal = translateNumberToDecimal(number)
    decimalNumbers.append(decimal)

  return decimalNumbers

def decimalToSanafu(decimal):
  inBase = fromDecimalToBase(decimal, 5)

  patata = []
  for digit in inBase:
    transalted = translateDigitInBase5ToSnafu(digit)
    patata.append(transalted)
  
  print(f"Numero sin fixear: {patata}")
  result = fixMultiDigit(patata)
  return result

def fromDecimalToBase(decimal, base):

  restos = []
  entera = decimal
  
  while entera >= base:
    resto = entera % base
    restos.append(resto)
    entera = entera // base

  restos.append(entera)
  restos.reverse()

  return restos

def translateDigitInBase5ToSnafu(digit):
  if digit == 4: return "1-"
  if digit == 3: return "1="
  return str(digit)

def fixMultiDigit(digits):
  digits.reverse()

  result = []
  numDigits = len(digits)

  for position in range(numDigits):
    
    digit = digits[position]
    if len(digit) > 1:

      if position != numDigits -1:

        result.append(digit[1])
        loQueMellevo = digit[0]
        fixedDigit = sumSnafu(loQueMellevo, digits[position+1])


        print(f"Fixeado: {fixedDigit}")
        digits[position+1] = fixedDigit
        print(digits)
      else:
        result.append(digit)
    
    else:
      result.append(digit)

  result.reverse()
  return result

def sumSnafu(loQueMellevo, num):
  if num == "0": return "1"
  if num == "1": return "2"
  if num == "2": return "1="
  if num == "1=": return "1-"
  if num == "1-": return "10"

  print("Esto no me lo esperaba")