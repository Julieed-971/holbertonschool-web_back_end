export default function createInt8TypedArray(length, position, value) {
  // Return a new array buffer with an Int8 value at a specific position
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);
  view.setInt8(position, value);
  return view;
}
