// -*- mode:c++;tab-width:2;indent-tabs-mode:t;show-trailing-whitespace:t;rm-trailing-spaces:t -*-
// vi: set ts=2 noet;
//
// (c) Copyright Rosetta Commons Member Institutions.
// (c) This file is part of the Rosetta software suite and is made available under license.
// (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
// (c) For more information, see http://www.rosettacommons.org. Questions about this can be
// (c) addressed to University of Washington UW TechTransfer, email: license@u.washington.edu.

/// @file ___FILENAME___
///
/// @brief
/// @author ___FULLUSERNAME___



#ifndef INCLUDED____FILEBASENAMEASIDENTIFIER____HH
#define INCLUDED____FILEBASENAMEASIDENTIFIER____HH

class ___FILEBASENAME___ : public protocols::moves::Mover
{
public:
	___FILEBASENAME___();
	virtual ~___FILEBASENAME___();

	virtual void apply( Pose & pose );
	virtual std::string get_name() const;

	virtual protocols::moves::MoverOP clone() const;
	virtual protocols::moves::MoverOP fresh_instance() const;

	virtual void parse_my_tag(
		TagPtr const tag,
		protocols::moves::DataMap &,
		Filters_map const &,
		protocols::moves::Movers_map const &,
		Pose const &
	);

};

#endif

