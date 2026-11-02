import React from 'react'

import Link from 'next/link'


export default function NavBar() {
  return (
    <nav className=' p-6 bg-white text-black  flex flex-row justify-between  gap-10  w-[90%]'>
        <h2 className='text-2xl font-extrabold text-gray-500 mr-100'>BrotherHood</h2>
        <div className='gap-x-6 flex flex-row font-semibold  '>
            <Link href={'/'} className=' hover:underline p-2 rounded transiton duration-400 ease-in-out'>home</Link>
            <Link href={'/dashboard'} className='hover:bg-gray-500 hover:text-white p-2 rounded transiton-.2s'>dashboard</Link>
            <Link href={'/about'} className='hover:bg-gray-500 hover:text-white p-2 rounded transiton-.2s'>about</Link>

        </div>
  
    </nav>
  )
}
