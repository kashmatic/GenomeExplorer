<?php require ('../template/header.php'); ?>

<section class="content-header">
  <h1>Hierarchical cluster</h1>
</section>

<section class="content">
	<div class="box box-success">
		<div class="box-body">
    		<div class="row">
    			<div class="col-md-8">
    				<h4>Filter by Experiments:</h4>
    				<?php include ("experiments.php") ?>
    			</div><!-- col-md-8 -->
    			<div class="col-md-4">
    				<h4>Gene list:</h4>
    				<textarea id="hc_genelist" rows="10" type="text" class="form-control"><?php echo file_get_contents( "cluster.example.genes" );?></textarea>
					<h4>Agglomeration method:</h4>
					<select id="hc_method" class="form-control">
						<option value="average" selected>average</option>
						<option value="centroid">centroid</option>
						<option value="complete">complete</option>
						<option value="median">median</option>
						<option value="mcquitty">mcquitty</option>
						<option value="single">single</option>
						<option value="ward">ward</option>
					</select>
					<h4>Distance calculation:</h4>
					<select id="hc_dist" class="form-control">
						<option value="euc" selected>Euclidean</option>
						<option value="cor">Correlation</option>
					</select>
				</div><!-- col-md-4 -->
			</div><!-- row -->

			<?php require ("../mysql/database_connect.php"); ?>
			<button class="btn btn-success" style="width:100px" onclick="run_hclust()">Run</button>
			<input type="hidden" name="run_hclust_path" value="<?php if ($_SESSION['user']['email']) { echo $_SESSION['user']['email'];} else { echo "guest";} ?>">
			<br><span id="spinner" style="display: none"><img src="/img/ajax-loader1.gif"></span>
		
			<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>
			<script src="/js/jscharts.js" type="text/javascript"></script>
			<script src="/js/cluster.js" type="text/javascript"></script>
		</div><!-- box-body -->
	</div><!-- box -->

	<div id="div_hclust"></div>
</section>

<?php require ('../template/footer.php'); ?>