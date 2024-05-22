export default function createInt8TypedArray(length, position, value) {
  // Create an ArrayBuffer of the given length
  const buffer = new ArrayBuffer(length);

  // Create a DataView for the buffer
  const view = new DataView(buffer);

  // If the position is out of range, throw an error
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Set the value at the given position in the DataView as an 8-bit signed integer
  view.setInt8(position, value);

  // Return the DataView
  return view;
}
