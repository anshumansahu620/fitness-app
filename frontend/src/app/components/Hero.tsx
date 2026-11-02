import React from 'react'

export default function Hero() {
  return (
<div className='h-[50vh] w-[90%] bg-radial-[at_25%_25%] from-white to-zinc-900 to-75%"  rounded-2xl flex flex-col justify-center items-center text-white p-8 shadow-xl border border-gray-700 gap-4 border-none mt-10'>
  <div className='w-full text-5xl font-extrabold tracking-wide mb-4 text-right'>
    <h5 className=' uppercase text-white'>Welcome to Brotherhood</h5>
  </div>

  <div className='text-left oslwald.className mt-10 text-lg leading-relaxed w-[95%] opacity-90  text-white'>
    <p>Empowering your fitness journey with smart solutions</p>
    <p>and expert guidance to overcome every gym challenge.</p>
  </div>

  <div className='w-[95%] gap-2 flex flex-row items-center mt-6'>
  <button className='p-2 px-4 rounded-xl text-lg font-semibold border hover:bg-white hover:text-black transition-all border-white duration-300'>
    Get Started
  </button>
  <button className='p-2 px-4 rounded-xl text-lg font-semibold border bg-white text-black border-gray-500 '>
    Know More
  </button>
</div>

</div>


  )
}
