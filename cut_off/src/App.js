import {Routes,Route} from 'react-router-dom'
import FrontPage from './routes/FrontPage/FrontPage';
import NIT from './routes/NIT/NIT';
import IIT from './routes/IIT/IIT';
import TopCollege from './routes/TopColleges/TopColleges.js';
function App() {
  return (
  <>
  <Routes>
    <Route path='/' element={<FrontPage />} />
    <Route path='/:id' element={<NIT />} />
    <Route path='/:id' element={<IIT />} />
    <Route path='/topcollege' element={<TopCollege />} />
  </Routes>
  </>
  );
}

//flask+react
// import React, { useEffect} from "react";
// import FrontPage from './routes/FrontPage/FrontPage';
// // import IIT from './routes/IIT/IIT';

// const useFlaskData = (url) => {

//   useEffect(() => {
//       fetch(url)
//           .then(response => response.json())
//   }, [url]);
// };

// function Comp1(){
//   useFlaskData('/');
//   return (
//     <>
//     <FrontPage />
//     </>
//   )
// }
// // function Comp2(){
// //   useFlaskData('/:id');
// //   return (
// //     <>
// //     <IIT />
// //     </>
// //   )
// // }
// const App = () => {
//   return (
//     <>
//       <Comp1 />
//       {/* <Comp2 /> */}
//     </>
//   );
// };

export default App;
